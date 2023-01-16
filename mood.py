#emotion_detection.py
import cv2
from deepface import DeepFace
import numpy as np  #this will be used later in the process

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        continue
    # image = cv2.imread(imgpath)

    analyze = DeepFace.analyze(image,actions=['emotion','age'])  #here the first parameter is the image we want to analyze #the second one there is the action
    print(analyze)
    cv2.imshow('very good emo', image)
    cv2.waitKey(0)