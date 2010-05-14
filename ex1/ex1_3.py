
import pylab as plt
from image_tools import *

image_path  = "./images/"
img_type    = "tiff"

chosen_one  = get_random_image(image_path, img_type)
rand_img    = load_image(chosen_one)
plt.imshow(rand_img)
plt.gray()
plt.title(chosen_one)

patch = get_random_patch(rand_img)
normedPatch = norm_patch(patch)

plt.figure()
plt.imshow(normedPatch)
plt.show()



