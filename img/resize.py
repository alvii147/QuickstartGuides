import os
from PIL import Image

def imgResize(img, width = None, height = None):
    if width == None and height == None:
        return img

    if width == None:
        new_size = (getProportionalWidth(img, height), height)
    elif height == None:
        new_size = (width, getProportionalHeight(img, width))
    else:
        new_size = (width, height)

    return img.resize(new_size, Image.ANTIALIAS)

def getProportionalWidth(img, height):
    return int(height * (img.size[0] / img.size[1]))

def getProportionalHeight(img, width):
    return int(width * (img.size[1] / img.size[0]))

if __name__ == '__main__':
    for filename in os.listdir():
        if filename.endswith('.png') or filename.endswith('jpg'):
            img = Image.open(filename)
            img = imgResize(img, height = 75)
            img.save('resized/' + filename)