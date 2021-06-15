# import libraries
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from skimage.feature import register_translation

# define function
def translateimage(i1, i2):
    ''' Takes an input of two images and registers the translation between them. Then translates the second image to better match the first one '''
    # read images and convert to grayscale
    im1 = np.asarray(Image.open(i1).convert("L"))
    im2 = np.asarray(Image.open(i2).convert("L"))

    # Find the x,y shift
    shift, error, diffphase = register_translation(im1, im2)
    print (shift)

    # shift the second image to align with the first
    y, x = np.shape(im1)
    print (type(x), type(y))
    iy, ix = shift #change to int so it will work please thanks.
    print (type(ix), type(iy))
    im2reg = im2[y + iy, x + ix]

    # plot images
    plt.subplot(221)
    plt.imshow(im1,cmap='Greys')
    plt.title('Reference')
    plt.subplot(223)
    plt.imshow(im2,cmap='Greys')
    plt.title('Shifted')
    plt.subplot(222)
    plt.title('Aligned')
    plt.imshow(im2reg,cmap='Greys')

    return

    if __name__ == "__main__":
        print ("Aligning images using register_translation")
