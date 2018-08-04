from astropy.io import fits
from numpy import unravel_index
import numpy as np
import matplotlib.pyplot as plt

def load_fits(file) :
    hdulist = fits.open(file)
    data = hdulist[0].data
    theArgMax = np.argmax(data)
    var = unravel_index(theArgMax, data.shape)
    return var

def drightest_pixel(filename):
  hdulist = fits.open(filename)
  data = hdulist[0].data

  arg_max = np.argmax(data)  
  max_pos = np.unravel_index(arg_max, data.shape)
  
  return max_pos
    

if __name__ == '__main__':
  #bright = load_fits('image1.fits')
  #print(bright)

  #hdulist = fits.open('image1.fits')
  #data = hdulist[0].data

  # Plot the 2D image data
  #plt.imshow(data.T, cmap=plt.cm.viridis)
  #plt.colorbar()
  #plt.show()