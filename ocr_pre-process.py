import cv2
import numpy as np

img = cv2.imread('image.jpg')

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#dilation:  adds pixels to the boundaries of objects in an image, while erosion removes pixels on object boundaries.  
# The rule used to process the pixels defines the operation as a dilation or an erosion
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
#erosion: morphological image processing from which all other morphological operations are based. 
# It was originally defined for binary images, later being extended to grayscale images, and subsequently to complete lattices.
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)
#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


#25/07/21
#skew correction bug report: angle bug resulting in var angle not being registered 
#def deskew(image):
#    coords = np.column_stack(np.where(image > 0))

#    angle = cv2.minAreaRect(coords)[-1]
#     if angle < -45:
#        angle = -(90 + angle)
#    else:
#        angle = -angle
#    (h, w) = image.shape[:2]
#    center = (w // 2, h // 2)
#    M = cv2.getRotationMatrix2D(center, angle, 1.0)
#    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
#    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 