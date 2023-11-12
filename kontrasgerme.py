import cv2
import numpy as np

image = cv2.imread('C:/Users/yasin/Desktop/Pictures/picture2.jpg')


min_val = 100
max_val = 255

#  kontrast genişletme formülünü 
Bit_o = ((image - min_val) / (max_val - min_val)) * 255
Bit_o = Bit_o.astype(np.uint8)


cv2.imshow('Doğrusal Kontrast Genişletme', Bit_o)
cv2.waitKey(0)
cv2.destroyAllWindows()