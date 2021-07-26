# import libraries
import matplotlib.pyplot as plt
import cv2
import numpy as np
from skimage.feature import register_translation
import pandas as pd

# define function
def translateimage(i1, i2):
    ''' Takes an input of two images and registers the translation between them.
    Then translates the second image to better match the first one '''
    # read images and convert to grayscale
    im1 = np.asarray(cv2.imread(i1, 0))
    im2 = np.asarray(cv2.imread(i2, 0))

    # Find the x,y shift
    shift, error, diffphase = register_translation(im1, im2)
    print (shift)

    # shift the second image to align with the first
    y, x = np.shape(im1)
    print (type(x), type(y))
    iy, ix = shift
    print (type(ix), type(iy))
    trans_matrix = np.float32([[1,0,iy], [0,1,ix]])
    rows, cols = im2.shape
    im2reg = cv2.warpAffine(im2, trans_matrix, (cols,rows))

    # plot images
    plt.subplot(221)
    plt.imshow(im1,cmap='Greys')
    plt.title('Reference')
    plt.subplot(222)
    plt.imshow(im2,cmap='Greys')
    plt.title('Shifted')
    plt.subplot(223)
    plt.title('Aligned')
    plt.imshow(im2reg,cmap='Greys')

    return

if __name__ == "__main__":
    print ("Aligning images using register_translation")

#------------------------------------------------------------------------------

#define function
def wavetxt2waveframe(txtlist):
    '''Takes a list of multiple years of .txt files from a NDCB buoy
    standard meteorological data and returns a single pandas dataframe
    that only contains wave height, dominant period, wave direction,
     and a timestamp in the form of a pandas datetime object'''

    # create an empty list that will hold the opened txt files
    framelist = []

    # Loop through each txt file and read it into a pandas dataframe
    for txt in txtlist:
        framelist.append(pd.read_csv(txt, skiprows=range(1,2), delim_whitespace = True, \
                                     parse_dates={'date':[0,1,2,3,4]}, keep_date_col=False))

    # concatenate the dataframes
    waveframe = pd.concat(framelist, ignore_index = True)

    # Transfer data in "date" column to a column where it is stored as a datetime object
    waveframe['Timestamp'] = pd.to_datetime(waveframe['date'], format = '%Y %m %d %H %M')


    # There must be a more pythonic way to index through these
    waveframe = waveframe.drop(waveframe.columns[[0,1,2,3,6,8,9,10,11,12, 13]], axis = 1)

    # Remove rows that have no information for either wave height or period
    waveframe = waveframe.replace(to_replace = 99.00, value = np.nan)
    waveframe = waveframe.dropna()

    return waveframe

def readwavetxt(fn):
    '''Take a  txt file and return a dataframe'''
    df = pd.read_csv(fn, skiprows=range(1,2), delim_whitespace = True, \
                    parse_dates={'date':[0,1,2,3,4]}, keep_date_col=False)

    # Transfer data in "date" column to a column where it is stored as a datetime object
    df['datetime'] = pd.to_datetime(df['date'], format = '%Y %m %d %H %M',utc=True)
    df = df.drop(df.columns[[0,1,2,3,6,8,9,10,11,12, 13]], axis = 1)

    # calculate unix datetime
    df['epoch']=(df['datetime'] - pd.Timestamp("1970-01-01",tz='utc')) // pd.Timedelta('1s')

    # remove data with NaN values
    df = df[df['WVHT'] < 99.0]
    df = df[df['DPD'] <99.0]
    df = df[df['MWD'] < 999]

    print (df.head())

    # put data frame into a numpy array
    waves = df[df.columns[[4,0,1,2]]].to_numpy()
    print('array with shape',np.shape(waves))


    return waves

#-------------------------------------------------------------------------------

def waveframetocsv (nnf, linf, firsttime, csvfile, owgtrainimgs, directory, source, destination):
    '''
    This function takes a prepared waves dataframe and filters
    and moves imgaes into the appropirate created foldersfor OWG training.

    nnf is a nearest neighbor interpolator of waves
    linf is a linear interpolator of waves
    firsttime is the pandas datetime string of the first entry from waves
    csvfile is the name of the csvfile being created
    owgtrainimgs is the name of the folder that will hold the training images
    directory is the directory of images that have been prepped for OWG filtering
    source is the name of files in the directory
    dstination is the name of the files oncw they are sent to the owgtrainimgs folder'''
    # create csv file that will be appended to by loop
    with open(csvfile, "w") as text_file:
        text_file.write("id, H, T, MWDIR\n")

    # create directory that will hold images with wave data
    try:
        shutil.rmtree(owgtrainimgs)
        os.mkdir(owgtrainimgs)
    except:
        os.mkdir(owgtrainimgs)
        print("couldn't find folder, make new one")

    # delete the csv file
    try:
        os.remove(csvfile)
    except:
        print("couldn't find file, making new one")

    counter = 0
    timecounter = 0
    nightcounter = 0
    blurcounter = 0
    failcounter = 0

    #check first time in record
    firsttime = (pd.Timestamp(firsttime)-pd.Timestamp('1970-01-01')) // pd.Timedelta('1s')
    print (firsttime)

    #loop through directory and interpolate files
    for filename in os.listdir(directory):
        # Use string slicing to remove .jpg from filename
        size = len(filename)
        fn = filename[:size - 4]

        # get time from filename
        ti = calendar.timegm(datetime.datetime.strptime(fn, "%Y%m%d%H%M").timetuple())

        try:
            # interpolate data that is within the interpolation range (aka only use images from when buoy was in water)
            if ti >= firsttime:
                zi = nnf(ti)
                wi = linf(ti)

            # find how many seconds elapsed between the image and the interpolated wave data
            timedif = abs(int(ti)-int(zi[0]))

            # Average image intensity
            avgintensity = np.mean(plt.imread(source.format(filename)))

            # Image Sharpness
            sharpness, contrast = estimate_sharpness(plt.imread(source.format(filename)))

            # if image was taken more than 30min from the wave data toss out image
            if timedif >= 1800:
                #print("{} exceeds maximum time allowance".format(filename))
                timecounter = timecounter + 1

            # if avg image intensity is below 40 (meaning it was taken at night) toss out image
            elif avgintensity < 40:
                #print("{} taken at night, passing over".format(filename))
                nightcounter = nightcounter + 1

            # if image sharpness is over 3.5 (the mean of sharpness for all images in 2017) toss out imaage
            elif sharpness < 3.5:
                #print ("{} is too blurry, passing over".format(filename))
                blurcounter = blurcounter + 1

            else:
                with open(csvfile, "a") as text_file:
                    text_file.write("{0:s},{1:0.2f},{2:0.2f},{3:0.2f}\n".format(filename,wi[0],wi[1],zi[3]))

                #print('moving {} from {} to {}'.format(filename, source, destination))

                # move images from prep folder into the training folder
                shutil.copy(source.format(filename), destination.format(filename))

                # document that a file has been moved to the training folder
                counter = counter + 1


        except:
            failcounter = failcounter + 1


    print (counter+nightcounter+timecounter+blurcounter+failcounter, "images found")
    print (failcounter, "images outside of interpolation range")
    print(timecounter, "images removed from training dataset due to no availablae wave data withing 30 minutes")
    print(blurcounter, "images removed from training dataset due to insufficient sharpness score")
    print(nightcounter, "images removed from training dataset due to inusfficeint intensity score")
    print (nightcounter+timecounter+blurcounter+failcounter, "total images removed from training dataset")
    print (counter, "images moved to OWG training folder")
    return

#-------------------------------------------------------------------------------

def prepowgimgs(year, directory, arrayshape, resolution, version):
    '''Create a new directory of images and prepare them for further data filtering. version 1.0
    Year is the target year of images,
    directory is where the year files are stored,
    resolution is the resolutiont the images will be reduced to,
    version is the version that these inputs are associate with. A record of this should be kept by hand.
    '''
    # create a new directory with the called year_imgprep
    print("Creating folder")
    foldername = "/{}_imgprep".format(str(year))
    newdir = directory+foldername+"{}".format(version)
    try:
        shutil.rmtree(newdir)
        print("Folder found: deleting contents")
        os.mkdir(newdir)
    except:
        os.mkdir(newdir)

    # copy files into new directory, this can take a while
    print("Moving Files")
    copy_tree(directory+"/{}".format(str(year)), newdir)


    # seperate the views into different folders within the directory
    print("Seperating Views")
    view1path = newdir+"/view1"
    view2path = newdir+"/view2"
    os.mkdir(view1path)
    os.mkdir(view2path)
    for filename in os.listdir(newdir):
        if filename.endswith(".01.jpg"):
            os.rename(newdir+"/{}".format(filename), view1path+"/{}".format(filename.replace(".01","")))
        elif filename.endswith(".02.jpg"):
            os.rename(newdir+"/{}".format(filename), view2path+"/{}".format(filename.replace(".02","")))

    # edit images from desired view into cropped lower resolution grayscale and store in new folder
    print ("Editing images for analysis")
    for filename in os.listdir(view2path):
        if filename.endswith(".jpg"):
            image = Image.open(view2path+"/{}".format(filename))
            #convert image to grayscale
            bw = image.convert("L")
            # select target portion of image to make it square
            bwarray = np.array(bw)
            small = bwarray[arrayshape]
            small_img = Image.fromarray(small)
            # change image resoltuion
            resize = (resolution, resolution)
            smaller = small_img.resize(resize)
            # save images ready for interpolation and filtering as the same name sans underscore seperating date and time
            try:
                smaller = smaller.save(view2path+"/"+filename)
            except IOError:
                print("cannot create image for", filename)
            # remove the underscore in the filename
            os.rename(view2path+"/"+filename, view2path+"/"+filename.replace("_",""))

    return print ("Completed.")
#-------------------------------------------------------------------------------
def estimate_sharpness(img):
    """
    Estimate image sharpness and contrast
    Input:
        img - np.ndarray representing image
              img read as skimage.io.imread( 'imagefilename.jpg' )
    Returns:
        s,c - sharpness and contrast estimates

    adapted from https://stackoverflow.com/questions/6646371/detect-which-image-is-sharper
    """
    contrast = img.std()
    gy, gx = np.gradient(img)
    gnorm = np.sqrt(gx**2 + gy**2)
    sharpness = np.average(gnorm)
    return sharpness, contrast
# edited to remove the part where they convert to grayscale as my images already are grayscale. 
