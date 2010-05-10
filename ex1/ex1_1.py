
import Image
import numpy as np
import pylab as plt
from scipy.signal import convolve2d




sigmas = [100, 1000, 5000, 10000, 30000]

def load_image(path):
    im = Image.open(path)
    im_ar = np.array(im.getdata())
    return np.reshape(im_ar, (im.size[1], im.size[0]))

def add_noise(im, sigma):
    noise = np.random.randn(np.shape(im)[0], np.shape(im)[1]) * sigma
    return im + noise


i = load_image('/home/mohbf/images/imk00571.tiff')
plt.rcParams['image.interpolation'] = 'nearest'
plt.figure()
plt.gray()
plt.imshow(i)

"""
for sigma in sigmas:
    noisi = add_noise(i, sigma)
    plt.figure()
    plt.imshow(noisi)
plt.show()
"""

kernel_sizes    = [3, 5, 9, 15, 29]
sigma           = 5000
noise           = np.random.randn(np.shape(i)[0], np.shape(i)[1]) * sigma
for kernel_size in kernel_sizes:
    kernel      = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
    noise_conv  = convolve2d(noise, kernel, 'same')
    plt.figure()
    plt.imshow(i + noise_conv)
plt.show()
