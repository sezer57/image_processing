import cv2
import numpy as np
from scipy.ndimage import gaussian_filter
from scipy.signal import convolve2d


image = cv2.imread('C:/Users/yasin/Desktop/Pictures/picture2.jpg')

#ortalama alma filtre maskesi
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

smoothed_image = cv2.filter2D(image, -1, kernel)

cv2.imshow('Ortalama Alma İşlemi', smoothed_image)
cv2.waitKey(0)


#gauss filtersi
sigma = 1.0
size = 5
gauss_filter = np.fromfunction(
    lambda x, y: (1/ (2 * np.pi * sigma ** 2)) * np.exp(-((x - size//2) ** 2 + (y - size//2) ** 2) / (2 * sigma ** 2)),
    (size, size)
)
gauss_filter /= np.sum(gauss_filter)
print("5x5 Gauss Filtresi:")
print(gauss_filter)

smoothed_image = gaussian_filter(image, sigma)


cv2.imshow('Gauss İşlemi', smoothed_image)
cv2.waitKey(0)


#laplace filtersi 

laplace_filter = np.array([[0, 1, 0],
                           [1, -4, 1],
                           [0, 1, 0]])
sharpened_image = cv2.filter2D(image, -1,laplace_filter)

cv2.imshow('laplace İşlemi', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
