
import pylab as plt
from image_tools import *

image_path  = "/home/mohbf/images/"
im_type     = "tiff"

chosen_one  = get_random_image(image_path, im_type)
rand_i      = load_image(chosen_one)
plt.imshow(rand_i)
plt.gray()
plt.title(chosen_one)
plt.show()
