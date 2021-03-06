import cv2 as cv
import numpy as np

img = cv.imread('lines.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 120)
minLineLength = 20
maxLineGap = 5
lines = cv.HoughLinesP(edges, 1, np.pi/180.0, 20, minLineLength, maxLineGap)
No_lines,a,b = np.shape(lines)
print(No_lines)
for index in range(No_lines):
   
    for x1, y1, x2, y2 in lines[index]:
        cv.line(img, (x1, y1), (x2, y2), (0,255,0),2)
        cv.imshow("edges", edges)
        cv.imshow("lines", img)
cv.waitKey()