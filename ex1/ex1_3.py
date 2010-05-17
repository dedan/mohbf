import pylab as plt
from image_tools import *
import numpy as np

image_path  = "./images/"
img_type    = "tiff"
plt.rcParams['image.interpolation'] = 'nearest'

"""Loads a rando image from database, extracts and nomalizes a random patch of it
and plots both."""

chosen_one  = get_random_image(image_path, img_type)
rand_img    = load_image(chosen_one)
plt.imshow(rand_img)
plt.gray()
plt.title(chosen_one)

patch = get_random_patch(rand_img)
normedPatch = norm_patch(patch)

plt.figure()
plt.imshow(normedPatch)

n_patches = 10
patch_set = [get_random_patch(rand_img,16) for i in range(n_patches)]
normed_patch_set = norm_patch_set(patch_set)

flat = []
mean_patch = np.zeros(np.shape(patch_set[0]))
for patch in patch_set:
    mean_patch = mean_patch + patch
    flat.append(patch)
        
mean_patch  = mean_patch / len(patch_set)
print np.shape(flat)
var         = np.std(flat)

print np.mean(mean_patch)
print np.std(mean_patch)
plt.figure()
plt.imshow(normed_patch_set[0])
plt.show()

