import numpy as np
import cv2 as cv

def get_cont(img):
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.GaussianBlur(imgray, (7, 7), 0)
    thresh = cv.adaptiveThreshold(imgray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 31, 8)
    return thresh

if __name__=="__main__":

    cap = cv.VideoCapture(0)

    aa = 0
    while True:
        success, img = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue
        aa +=1
        img = get_cont(img)
        cv.imshow('aaaa', img)
        cv.waitKey(0)
