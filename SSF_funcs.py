# import libraries
import cv2
import numpy as np
from skimage.feature import register_translation
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime
import calendar
from scipy import interpolate
import os
import shutil
import csv

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
#-------------------------------------------------------------------------------
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

def waveframetocsv (nnf, linf, firsttime, csvfile, directory):
    '''
    This function takes a prepared waves dataframe and filters and moves imgaes into the appropirate created folders
    for OWG training.

    nnf is a nearest neighbor interpolator of waves
    linf is a linear interpolator of waves
    firsttime is the pandas datetime string of the first entry from waves
    csvfile is the name of the csvfile being created
    directory is the directory of images that have been prepped for OWG filtering
    '''

    # delete the csv file if it exsists
    try:
        print ("Overwriting csv file")
        os.remove(csvfile)
        with open(csvfile, "w") as text_file:
            text_file.write("id, H, T, MWDIR\n")
    except:
        print("couldn't find file, making new one")
        # create csv file that will be appended to by loop
        with open(csvfile, "w") as text_file:
            text_file.write("id, H, T, MWDIR\n")

    counter = 0
    failcounter = 0
    timecounter = 0

    #check first time in record as a unix timestamp
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

            # if image was taken more than 30min from the wave data toss out image
            if timedif >= 1800:
                timecounter = timecounter + 1

            # add image to the csv file
            else:
                with open(csvfile, "a") as text_file:
                    text_file.write("{0:s},{1:0.2f},{2:0.2f},{3:0.2f}\n".format(filename,wi[0],wi[1],zi[3]))


                # document that a file has been moved to the training folder
                counter = counter + 1

        except:
            failcounter = failcounter + 1


    print (failcounter, "images outside of interpolation range")
    print(timecounter, "images not included from training dataset due to no availablae wave data withing 30 minutes")
    print (timecounter+failcounter, "total images not included in training dataset")
    print (counter, "images added to {}".format(csvfile))
    return

#-------------------------------------------------------------------------------

def prepowgimgs(year, directory, arrayshape, resolution, trial, viewlist):
    '''Create a new directory for images in each view and run QC and primary augmentation before interpolation and then model
    training, validation, or testing. version 2.0

    Year is the target year of images,
    directory is where the year files are stored,
    resolution is the resolutiont the images will be reduced to,
    trial is the name of the trial that these inputs are associate with. A record of trial details should be kept by hand and stored
    in C:/njc/src/SSF/OWG/OWG_records/trial.
    viewlist is a list of the view numbers found in the target year folder
    '''
    start = time.time()
    #set counters
    counter = 0
    nightcounter = 0
    blurcounter = 0
    failcounter = 0

    # create a new directory with the called year_imgprep
    foldername = "/{}_imgprep".format(str(year))
    newdir = directory+foldername+"{}".format(trial)
    try:
        shutil.rmtree(newdir)
        print("Folder found: deleting contents")
        print("Creating folder")
        os.mkdir(newdir)
    except:
        print("Creating folder")
        os.mkdir(newdir)

    # copy files into new directory, this can take a while
    print("Moving Files")
    copy_tree(directory+"/{}".format(str(year)), newdir)

    # seperate the views into different folders within the directory
    viewdirs = []
    for view in viewlist:
        print("Seperating View {}".format(view))
        viewpath = newdir+"/view{}".format(view)
        viewdirs.append(viewpath)
        os.mkdir(viewpath)


    for viewpath in viewdirs:
        print ("Moving images to {}".format(viewpath))
        # move images into views
        for filename in os.listdir(newdir):
            if filename[-5] == viewpath[-1]:
                os.rename(newdir+"/{}".format(filename), viewpath+"/{}".format(filename.replace(filename[13:16],"")))

        # edit images from desired view into cropped lower resolution grayscale and store in new folder
        print ("Augmenting and filtering imgaes in {}".format(viewpath))
        for filename in os.listdir(viewpath):
            if filename.endswith(".jpg"):
                image = Image.open(viewpath+"/{}".format(filename)).convert("L")

                # select target portion of image to make it square
                bwarray = np.array(image)
                small = bwarray[arrayshape]

                # change image resoltuion
                img = Image.fromarray(small)
                resize = (resolution, resolution)
                smaller = img.resize(resize)

                #Get QC metrics
                sharpness = estimate_sharpness(np.asarray(smaller))
                avgintensity = np.mean(np.asarray(smaller))

                # perform QC
                if sharpness < 3.5 or avgintensity < 85:
                    os.remove(viewpath+"/"+filename)
                    failcounter = failcounter + 1
                else:
                    # save images to OWG directory
                    try:
                        counter = counter + 1
                        owgimage = smaller.save(viewpath+"/{}".format(filename))
                    except IOError:
                        print("cannot create image for", filename)
                        failcounter = failcounter + 1

                    # remove the underscore in the filename
                    os.rename(viewpath+"/"+filename, viewpath+"/"+filename.replace("_",""))

    print (failcounter, "images removed for quality control")
    print (counter, "images processed")
    end = time.time()
    return print ("Completed in {} minutes.".format((end - start)/60))
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
