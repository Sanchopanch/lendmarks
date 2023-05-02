import cv2 as cv
import pickle
def add_mask():
    file = open('rez.pkl', 'rb')
    frames = pickle.load(file)
    file.close()
    rez = frames[0]

    image = cv.imread('saved_video1.png')

    final = rez[1].copy()

    for y in range(final.shape[0]):
        for x in range(final.shape[1]):
            pix = final[y][x]
            pixIm = image[y][x]
            blue = pixIm[0]>pixIm[1]+50
            red = pixIm[2]>pixIm[1]+50
            if red:
                print('red point at '+str(x)+ ' '+ str(y))
                final[y][x] = rez[0][y][x]
            if blue:
                print('blue point at ' + str(x) + ' ' + str(y))
                final[y][x] = rez[2][y][x]
    cv.imshow('aaaa', final)
    cv.waitKey(0)
    cv.imwrite('saved_video_m.png', final)


if __name__=="__main__":
    add_mask()