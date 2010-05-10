
import numpy as np
import pylab as plt
from scipy.signal import convolve2d
from image_tools import *


sigmas = [100, 1000, 5000, 10000, 30000]

i = load_image('/home/mohbf/images/imk00571.tiff')
plt.rcParams['image.interpolation'] = 'nearest'
plt.figure()
plt.gray()
plt.imshow(i)

for sigma in sigmas:
    noisi = add_noise(i, sigma)
    plt.figure()
    plt.imshow(noisi)
    plt.title('image plus random noise, sigma: %d' % sigma)


kernel_sizes    = [3, 5, 9, 15, 29]
sigma           = 5000
noise           = np.random.randn(np.shape(i)[0], np.shape(i)[1]) * sigma
for kernel_size in kernel_sizes:
    kernel      = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
    noise_conv  = convolve2d(noise, kernel, 'same')
    plt.figure()
    plt.imshow(i + noise_conv)
    plt.title('image plus filtered noise, sigma: %d and kernelsize: %d' % sigma, kernel_size)
plt.show()

