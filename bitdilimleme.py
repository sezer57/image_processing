import cv2
import numpy as np

image = cv2.imread('C:/Users/yasin/Desktop/Pictures/para.jpg')


#bit dilimleme
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
bit_slices = []

for i in range(1, 9):
    bit_slice = (image >> i) & 1
    cv2.imshow('Bit Dilimleri', bit_slice)
    bit_slices.append(bit_slice * 255)  

combined_image = np.hstack(bit_slices)

cv2.imshow('Bit Dilimleri', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()