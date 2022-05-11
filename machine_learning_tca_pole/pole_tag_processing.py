import cv2 as cv
import pytesseract as pyt
import numpy as np
from matplotlib import pyplot as plt

pyt.pytesseract.tesseract_cmd = r'C:/Users/ESankar.CITYOFNELSON/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

image_file = r'C:\\Users\\ESankar.CITYOFNELSON\\Desktop\\Test-Images-Python\\high-voltage.png'
image = cv.imread(image_file, cv.IMREAD_GRAYSCALE)

img = cv.medianBlur(image,5)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
text = pyt.image_to_string(img)
print(text)