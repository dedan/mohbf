import mdp
import numpy
import pylab as plt
from image_tools import *

"""Performs a PCA on natural image, white noise, and filtered
white noise patches in vector representation. Uses 5000 40 x 40 patches and
analyzes the first 25 basis vectors."""

image_path  = "/home/mohbf/images/"
img_type    = "tiff"
plt.rcParams['image.interpolation'] = 'nearest'

numberPatches = 5000
patchSize     = 40
patches       = []

for i in range(numberPatches):
    currentImg = get_random_image(image_path, img_type)
    currentImg = load_image(currentImg)
    
    patch = get_random_patch(currentImg, patchSize)
    patch = patch.flatten(1)
    
    patches.append(patch)

patches = np.array(patches, float)
print np.shape(patches)

pici = mdp.nodes.PCANode()
pici.train(patches)
pc   = pici.get_projmatrix()

for i in range(25):
    plt.subplot(5,5,i+1)
    plt.imshow(np.reshape(pc[:,i], (patchSize,patchSize)),vmin=np.min(pc),vmax=np.max(pc))
    plt.gray()
plt.show()
    

