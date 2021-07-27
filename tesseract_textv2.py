import re
import cv2
import pytesseract
from pytesseract import Output


# regular expression pattern that will match with  OCR results to find the appropriate bounding boxes. 
# regex module and the image_to_data function for this. 
#   Regex model:is a sequence of characters that specifies a search pattern. 
#               Usually such patterns are used by string-searching algorithms 
#               to "find" or "find and replace" operations on strings, or for input validation. 
#   image_to_data function: a PIL fork; takes a pil image and converts to readable data in a 128x128 max resolution matrix
img = cv2.imread('invoice-sample.jpg')
d = pytesseract.image_to_data(img, output_type=Output.DICT)
keys = list(d.keys())

date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
    	if re.match(date_pattern, d['text'][i]):
	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
	        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)