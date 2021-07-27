#authors: Arudra Rao
#notes: image locater issue, var image present in 
# 			arg parser, 
# 			greyscale conversion, 
# 			Output, 
# 			Bounding box info

from PIL import Image
import pytesseract
import argparse
import cv2
import os

# construct the argument parse and parse the arguments
# object parser probelms: -i C:\\USERS\\ARUDRA RAO\\DESKTOP\\EXAMPLLE.JPEG [-p PREPROCESS]      
# ocr_v1.py: error: the following arguments are required: -i/--C:\\Users\\Arudra Rao\\Desktop\\examplle.jpeg
# parser issue locate image

ap = argparse.ArgumentParser()
ap.add_argument("-i", r"--C:\\Users\\Arudra Rao\\Desktop\\examplle.jpeg", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

###### Greyscale coversion V2 ##########
#image = cv2.imread('')

#gray = get_grayscale(image)
########################################

# check to see if we should apply thresholding to preprocess the image
if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	#if preprocess is needed, reroute to ocr_pre-process


# make a check to see if median blurring should be done to remove noise
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)
# write the grayscale image to disk as a temporary file so we can apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete the temp file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
# show the output images
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)

#Bounding box info
img = cv2.imread('')

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)