import cv2 as cv
from backgr import get_current_contour
import pickle

def saveVideo():
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 1200)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 800)

    frames = []
    while True:
        success, img = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue
        rez = [get_current_contour(img, 4),  get_current_contour(img, 8), get_current_contour(img, 15)]
        # rez = get_current_contour(img, 8)
        cv.imshow('aaaa', rez[1])
        key = cv.waitKey(0)
        # print(key)
        if key == 115 : # S
            frames.append(rez)
        elif key == 27: # ESC
            cv.imwrite('saved_video.png', rez[1])
            cv.imwrite('saved_video1.png', rez[1])
            file = open('rez.pkl', 'wb')
            pickle.dump(frames, file)
            file.close()
            return


if __name__=="__main__":
    saveVideo()