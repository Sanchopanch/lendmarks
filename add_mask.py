import cv2 as cv
import pickle
def add_mask():
    file = open('rez.pkl', 'rb')
    frames = pickle.load(file)
    file.close()
    image = cv.imread('saved_video1.png')
    result_video = []

    for rez in frames:
        final = rez[1].copy()
        for y in range(final.shape[0]):
            for x in range(final.shape[1]):
                pixIm = image[y][x]
                blue = pixIm[0]>pixIm[1]+50
                red = pixIm[2]>pixIm[1]+50
                if red:
                    print('red point at '+str(x)+ ' '+ str(y))
                    final[y][x] = rez[0][y][x]
                if blue:
                    print('blue point at ' + str(x) + ' ' + str(y))
                    final[y][x] = rez[2][y][x]
        result_video.append(final)
    cv.imshow('aaaa', final)
    cv.waitKey(0)
    cv.imwrite('saved_video_m.png', final)
    cv.imwrite('saved_video_mask.png', final)

    file = open('rez.pkl', 'wb')
    pickle.dump(result_video, file)
    file.close()

if __name__=="__main__":
    add_mask()