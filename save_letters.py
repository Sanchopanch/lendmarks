import cv2 as cv
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import pickle

def add_text(font_size):
    image = cv.imread('saved_video_m.png')
    fontpath = "font/JetBrainsMono-Light.ttf"
    b, g, r, a = 0, 0, 0, 0

    font = ImageFont.truetype(fontpath, font_size)
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    draw.text((50, 100), "Привет мир!", font=font, fill=(b, g, r, a))
    image = np.array(img_pil)

    cv.imshow('aaaa', image)
    cv.waitKey(0)
    cv.imwrite('aaa.png', image)


def get_letter_pix(letter, font_size):
    fontpath = "font/JetBrainsMono-Light.ttf"
    font = ImageFont.truetype(fontpath, font_size)
    x, y = int(font_size/2)+2  , font_size + 2

    blank = [[[255, 255, 255] for col in range(x)] for row in range(y)]
    npBlank = np.array(blank, np.uint8)
    img_pil = Image.fromarray(npBlank)
    draw = ImageDraw.Draw(img_pil)
    draw.text((0, -2), letter, font=font, fill=(0, 0, 0, 0))
    image = np.array(img_pil)

    # cv.imshow('letter '+letter, image)
    # cv.waitKey(0)
    return image

def show_alph(font_size):
    letters = list('CqT')
    for letter in letters:
        print(letter)
        im = get_letter_pix(letter, font_size)
        cv.imshow('letter ', im)
        cv.waitKey(0)

def save_alph(font_size):
    letters = list('QWTYUIOP{}|AFJL:ZXCVM<>?/.,mbvcxzasdfghjkl;qertyuiop[]!@#$%^&*()_-+=`~')
    rez = {}
    for letter in letters:
        print(letter)
        im = get_letter_pix(letter, font_size)
        rez[letter] = im

    print('ok')
    file = open('letters15.pkl', 'wb')
    pickle.dump(rez, file)
    file.close()

if __name__ == "__main__":
    # save_alph(9)
    # add_text(9)
    show_alph(9)
