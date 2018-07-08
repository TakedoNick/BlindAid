# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:46:57 2018

@author: sharmaalish
"""


# hide a short message (255 char max) in an image
# the image has to be .bmp or .png format
# and the image mode has to be 'RGB'

from PIL import Image


def encode_image(img, msg):
    length = len(msg)
    if length > 255:
        print("text too long! (don't exeed 255 characters)")
        return False
    if img.mode != 'RGBA':
        print("image mode needs to be RGBA")
        return False
    encoded = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b, a = img.getpixel((col, row))
            if row == 0 and col == 0 and index < length:
                asc = length
            elif index <= length:
                c = msg[index -1]
                asc = ord(c)
            else:
                asc = r
            encoded.putpixel((col, row), (asc, g , b))

            index += 1
    return encoded

original_image_file = "predictions.png"

img = Image.open(original_image_file)

encoded_image_file = "enc_" + original_image_file
secret_msg = raw_input("my message")
print("\n length of image:")
print(len(secret_msg))
img_encoded = encode_image(img, secret_msg)

if img_encoded:
    img_encoded.save(encoded_image_file)
    print("{} saved!".format(encoded_image_file))

    



