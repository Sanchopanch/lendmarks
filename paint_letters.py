import pickle
import numpy as np
import cv2 as cv

def get_best_letter(letters,  fragment, fragment_mask):

    min_dist = 9999999999.
    current_closest_letter = ' '
    closest_letter_pix = None
    y_size, x_size, _ = fragment.shape
    rating = 0
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
                currMaskRed = fragment_mask[y,x,0]

                sumP = currPix.sum()
                sumL = currLet.sum()
                if sumP > sumL:
                    current_distance = sumP - sumL
                else:
                    current_distance = sumL - sumP
                if currMaskRed>0:
                    rating += dist

                if sumL == 0:
                    continue
                aa +=1
                dist += current_distance

        dist = dist/aa
        if min_dist > dist:
            min_dist = dist
            current_closest_letter = key
            closest_letter_pix = letterPix.copy()
            # print(current_closest_letter+' dist='+str(min_dist))
    return current_closest_letter, closest_letter_pix, rating

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

    file = open('rez.pkl', 'rb')
    frames = pickle.load(file)
    file.close()

    image = cv.imread('saved_video_m.png')
    mask_rating = cv.imread('saved_video_mask.png')
    yPix, xPix, _ = image.shape
    colmns = int(xPix / x_size)
    rows = int(yPix / y_size)
    cv.imshow('initial', image)
    cv.waitKey(0)

    first_el = True

    html = 'export let mooveData = ['
    html2 = 'export let mooveData = ['
    for frame in frames:
        for shift_x in range(x_size):
            for shift_y in range(y_size):

            # frame = frames[0]
                wLetters = frame.copy()
                wLetters.roll(shift_x)
                wLetters.roll(shift_y, axis=0)

                if not first_el:
                    html += ','
                    html2 += ','
                first_el = False
                html += '\n{'
                html2 += '\n{'
                first_el2 = True

                rating_sum = 0
                for y in range(rows):
                    string_html2 = ''
                    for x in range(colmns):
                        # print(x, y)
                        y_coor = y * y_size
                        x_coor = x * x_size
                        fragment = frame[y_coor:y_coor + y_size, x_coor:x_coor + x_size]
                        fragment_mask = mask_rating[y_coor:y_coor + y_size, x_coor:x_coor + x_size]
                        if fragment.sum() == space:
                            print(' ', end = "")
                            string_html2 +=' '
                            continue
                        current_closest_letter, closest_letter_pix, rating = get_best_letter(letters, fragment, fragment_mask)
                        rating_sum += rating
                        wLetters[y_coor:y_coor + y_size, x_coor:x_coor + x_size] = closest_letter_pix
                        print(current_closest_letter, end="")
                        string_html2 += current_closest_letter
                        if not first_el2:
                            html +=','
                        html +=f'"x{x_coor}-y{y_coor}":"{current_closest_letter}"'
                        first_el2 = False
                    html2 +=f'"y{y_coor}":"{string_html2}'
                    print('|')
                    cv.imshow('current frame', wLetters.copy())
                    html += '}'

    html +='];'
    cv.imwrite('saved_video_final.png', wLetters)
    cv.waitKey(0)

    html_file = open("output.html", "wt")
    html_file.write(html)
    html_file.close()
    print('saved output.html')



if __name__ == "__main__":
    # find_letter()
    put_letters()