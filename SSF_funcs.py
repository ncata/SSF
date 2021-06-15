# import libraries
import matplotlib.pyplot as plt
import cv2
import numpy as np
from skimage.feature import register_translation

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
