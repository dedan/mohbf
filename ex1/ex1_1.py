
from image_tools import *
import pylab as plt
import numpy as np

image_path = '/home/mohbf/images/imk00571.tiff'

i = load_image(image_path)
plt.rcParams['image.interpolation'] = 'nearest'
plt.figure()
plt.gray()
plt.imshow(i)
plt.show()
