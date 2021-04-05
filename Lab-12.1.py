import cv2 as cv # importing cv2 library as cv
import sys    # importing sys

img = cv.imread('hockey.jpeg',1) #using the cv.imread function to find the image
res = cv.resize(img,None,fx=2.5, fy=2.5, interpolation = cv.INTER_CUBIC)

if img is None: #condition to let the user know if the picture does not exist
    sys.exit("The image could not be read.") 
cv.imshow('Photo', img)  # show the picture in an app

cv.waitKey(0) #use a keyboard key to close the window
cv.destroyAllWindows() # close all windows 