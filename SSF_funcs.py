# import libraries
import matplotlib.pyplot as plt
import cv2
import numpy as np
from skimage.feature import register_translation
import pandas as pd

# define function
def translateimage(i1, i2):
    ''' Takes an input of two images and registers the translation between them. Then translates the second image to better match the first one '''
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

#define function
def wavetxt2waveframe(txtlist):
    '''Takes a list of multiple years of .txt files from a NDCB buoy
    standard meteorological data and returns a single pandas dataframe that only contains
    wave height, dominant period, wave direction, and a timestamp in the form of a pandas datetime object'''

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
