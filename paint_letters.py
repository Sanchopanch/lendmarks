import pickle
import numpy as np
import cv2 as cv

def get_best_letter(letters,  fragment):

    min_dist = 9999999999.
    current_closest_letter = ' '
    closest_letter_pix = None
    y_size, x_size, _ = fragment.shape
    for key in letters:
        if key == ' ':
            continue
        letterPix = letters[key]
        dist = 0.
        aa = 0
        for y in range(y_size):
            for x in range(x_size):
                currPix = fragment[y,x]
                currLet = letterPix[y,x]

                sumP = currPix.sum()
                sumL = currLet.sum()
                if sumL == 0:
                    continue
                aa +=1
                if sumP > sumL:
                    dist += sumP - sumL
                else:
                    dist += sumL - sumP
        dist = dist/aa
        if min_dist>dist:
            min_dist = dist
            current_closest_letter = key
            closest_letter_pix = letterPix.copy()
            # print(current_closest_letter+' dist='+str(min_dist))
    return current_closest_letter, closest_letter_pix

def find_letter():
    x_size, y_size = 9, 17
    file = open('letters15.pkl', 'rb')
    letters = pickle.load(file)
    file.close()

    x_coor, y_coor = 513, 89

    image = cv.imread('saved_video_m.png')
    fragment = image[y_coor:y_coor+y_size,x_coor:x_coor+x_size]
    cv.imshow('aaaa', fragment)

    current_closest_letter, closest_letter_pix = get_best_letter(letters,  fragment)

    cv.imshow('let', closest_letter_pix)
    cv.waitKey(0)

def put_letters():
    file = open('letters15.pkl', 'rb')
    letters = pickle.load(file)
    file.close()
    some_letter = letters['a']
    space = np.array([[[255,255,255] for x in range(some_letter.shape[1])] for y in range(some_letter.shape[0])]).sum()
    y_size, x_size, _ = some_letter.shape

    image = cv.imread('saved_video_m.png')
    yPix, xPix, _ = image.shape
    colmns = int(xPix / x_size)
    rows = int(yPix / y_size)
    cv.imshow('initial', image)
    cv.waitKey(0)

    wLetters = image.copy()
    html = ''
    for y in range(rows):
        for x in range(colmns):
            print(x, y)
            y_coor = y * y_size
            x_coor = x * x_size
            fragment = image[y_coor:y_coor + y_size, x_coor:x_coor + x_size]
            if fragment.sum() == space:
                continue
            current_closest_letter, closest_letter_pix = get_best_letter(letters, fragment)

            wLetters[y_coor:y_coor+y_size, x_coor:x_coor + x_size] = closest_letter_pix
            print(current_closest_letter)
            html +=f'<div style="top:{y_coor}px;left:{x_coor}px;">{current_closest_letter}</div>'

    cv.imshow('aaaa', wLetters)
    cv.waitKey(0)

    html_file = open("output.html", "wt")
    html_file.write(html)
    html_file.close()
    print('saved output.html')



if __name__ == "__main__":
    # find_letter()
    put_letters()