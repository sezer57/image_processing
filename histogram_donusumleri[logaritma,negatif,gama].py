import cv2
import numpy as np

image = cv2.imread('C:/Users/yasin/Desktop/Pictures/log.jpeg', cv2.IMREAD_GRAYSCALE)

# Logaritma dönüşümü 
c = 255 / np.log(1 + np.max(image))
log_transformed = c * (np.log(image + 1))

log_transformed = np.uint8(log_transformed)

cv2.imshow('Orjinal Görüntü', image)
cv2.imshow('Logaritma Dönüşümü', log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()

# negatif dönüşümü

log_transformed = 256 - 1 - image

log_transformed = np.uint8(log_transformed)

cv2.imshow('Orjinal Görüntü', image)
cv2.imshow('negatif Dönüşümü', log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Gama dönüşümü
gamma = 1.5 

gama_corrected = np.power(image / 255.0, gamma) * 255.0
gama_corrected = np.uint8(gama_corrected)

cv2.imshow('Orjinal Görüntü', image)
cv2.imshow('Gama Düzeltme', gama_corrected)


cv2.waitKey(0)
cv2.destroyAllWindows()
