# pip install opencv-python
# pip install pytesseract

# Use above commands to install the required libraries


import cv2
import pytesseract

# user need to install tesseract exe file

pytesseract.pytesseract.tesseract_cmd=r'C:\tesseract\tesseract.exe'

# Read the image of which you want to extract the text
img=cv2.imread('OCR2.jpg')
text=pytesseract.image_to_string(img)
print(text,end='')
