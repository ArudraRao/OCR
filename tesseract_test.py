#Author: Arudra Rao

import cv2
import pytesseract
from pytesseract import Output
d
#in_example includes bound box examples
img = cv2.imread('in_example.jpg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())

#to plot boxes:

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)



#osamu, from osamacorp, cyborg, oxygen makes me lose rationality so i always have a mask on, 
#sociopathic senses increase at mask loss, major hate for AI, bounty hunter for only AI,
#likes lego walls
#Sociopathy: indentified by right index finger twitch
#drugs calm me down
#augmentations: one arm, both legs, eye (figuring if there is a bounty or not) + increased insanity
#weapons: Guns + Laser Knife
# 
#  
#nestle: AI area
#Arasaka: human area
#osama: no onne gives a fuck
#
#my nnew mark: B370 leg set, a major associate in the nestle company