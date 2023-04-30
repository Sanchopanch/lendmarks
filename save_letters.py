import cv2 as cv
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import pickle

def add_text():
    image = cv.imread('saved_video_m.png')
    fontpath = "font/JetBrainsMono-Light.ttf"
    b, g, r, a = 0, 0, 0, 0

    font = ImageFont.truetype(fontpath, 15)
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    draw.text((50, 100), "Привет мир!", font=font, fill=(b, g, r, a))
    image = np.array(img_pil)

    cv.imshow('aaaa', image)
    cv.waitKey(0)
    cv.imwrite('aaa.png', image)


def get_letter_pix(letter):
    fontpath = "font/JetBrainsMono-Light.ttf"
    font = ImageFont.truetype(fontpath, 15)
    x, y = 9 , 17

    blank = [[[255, 255, 255] for col in range(x)] for row in range(y)]
    npBlank = np.array(blank, np.uint8)
    img_pil = Image.fromarray(npBlank)
    draw = ImageDraw.Draw(img_pil)
    draw.text((0, -3), letter, font=font, fill=(0, 0, 0, 0))
    image = np.array(img_pil)

    # cv.imshow('letter '+letter, image)
    # cv.waitKey(0)
    return image

if __name__ == "__main__":
    # add_text()
    letters = list('QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?/.,mnbvcxzasdfghjkl;qwertyuiop[]!@#$%^&*()_-+=')
    rez = {}
    for letter in letters:
        print(letter)
        im = get_letter_pix(letter)
        rez[letter] = im

    print('ok')
    file = open('letters15.pkl', 'wb')
    pickle.dump(rez, file)
    file.close()