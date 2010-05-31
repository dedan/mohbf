import mdp
import numpy
import pylab as plt
from image_tools import *

"""Train independent component analysis (ICA) on natural image patches in vector repre-
sentation. Use at least 5000 32 times 32 patches and reduce the dimensionality with PCA
to 256 dimensions. How do the resulting basis vectors look like?
To perform ICA you can use the package mdp (use the FastICA implementation, with a
symmetric optimization approach and a tanh non-linearity)."""

image_path  = "/home/mohbf/images/"
img_type    = "tiff"
plt.rcParams['image.interpolation'] = 'nearest'

numberPatches = 500
patchSize     = 32
patches       = []

for i in range(numberPatches):
    currentImg = get_random_image(image_path, img_type)
    currentImg = load_image(currentImg)
    
    patch = get_random_patch(currentImg, patchSize)
    patch = patch.flatten(1)
    
    patches.append(patch)

patches = np.array(patches, float)

pici = mdp.nodes.PCANode()
print pici.execute(patches, 256)

"""
pc   = pici.get_projmatrix()

for i in range(25):
    plt.subplot(5,5,i+1)
    plt.imshow(np.reshape(pc[:,i], (patchSize,patchSize)),vmin=np.min(pc),vmax=np.max(pc))
    plt.gray()
plt.show()
    
"""
