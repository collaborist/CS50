"""
The program helps perform augmentation of test images for a neural network.

"""

import os
import sys
from PIL import Image, ImageFilter
import argparse
import numpy as np
from random import randint, sample, shuffle

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-file", help="path of file", default='./', type=str)
    parser.add_argument("-r", help="degrees counter-clockwise rotation. for clockwise rotation use negative degrees", type=int)
    parser.add_argument("-f", help="flip image horizontal (h) or vertical (v)", type=str)
    parser.add_argument("-cb", help="cropping a subrectangle box from an image", nargs=4, type=int)
    parser.add_argument("-cr", help="cropping a random subrectangle from an image", type=int, choices=range(1, 100))
    parser.add_argument("-fltr", help="apply a filter on an image", type=str, choices=['blur','contour','detail','edge_enhance','edge_enhance_more','emboss','find_edges','sharpen','smooth','smooth_more'])
    parser.add_argument("-clr", help="change color of an image", type=int)
    parser.add_argument("-rgb", help="swap r, g, and b parameters of an image", action='store_true')
    args = parser.parse_args()

    path = args.file
    if not os.path.isdir(path):
        try:
            im = Image.open(path)
        except:
            sys.exit("Wrong path")
        name = path.split('/')[-1]
        name, format = name.split('.')
        print(name, format)
        if args.r:
            im = rotate(im, args.r)
            name = "r" + str(args.r) + "_" + name
        if args.f:
            im = flip(im, args.f)
            name = "f" + args.f + "_" + name
        if args.cb:
            im = cropbox(im, tuple(args.cb))
            name = "cb" + "-".join(map(str, args.cb)) + "_" + name
        if args.cr:
            im = croprand(im, args.cr)
            name = "cr" + str(args.cr) + "_" + name
        if args.fltr:
            im = fltr(im, args.fltr)
            name = "fltr" + args.fltr + "_" + name
        if args.clr:
            im = color(im, args.clr)
            name = "clr" + str(args.clr) + "_" + name
        if args.rgb:
            im = rgb(im)
            name = "rgb_" + name
        output(im, "proc_" + name + "." + format)
        return

    for filename in os.listdir(path):
        try:
            im = Image.open(os.path.join(path, filename))
        except:
            continue
        name, format = filename.split('.')
        if args.r:
            im = rotate(im, args.r)
            name = "r" + str(args.r) + "_" + name
        if args.f:
            im = flip(im, args.f)
            name = "f" + args.f + "_" + name
        if args.cb:
            im = cropbox(im, tuple(args.cb))
            name = "cb" + "-".join(map(str, args.cb)) + "_" + name
        if args.cr:
            im = croprand(im, args.cr)
            name = "cr" + str(args.cr) + "_" + name
        if args.fltr:
            im = fltr(im, args.fltr)
            name = "fltr" + args.fltr + "_" + name
        if args.clr:
            im = color(im, args.clr)
            name = "clr" + str(args.clr) + "_" + name
        if args.rgb:
            im = rgb(im)
            name = "rgb_" + name
        output(im, "proc_" + name + "." + format)

def rotate(image, degree):
    return image.rotate(degree)

def flip(image, type):
    if type == "h":
        return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    elif type == "v":
        return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    sys.exit("Wrong flip parameter")

def cropbox(im, box):
    width = im.size[0]
    height = im.size[1]
    if box[0] > width or box[2] > width:
        sys.exit("Wrong cropping width parameter(s)")
    elif box[1] > height or box[3] > height:
        sys.exit("Wrong cropping height parameter(s)")
    return im.crop(box)

def croprand(im, percent):
    width = im.size[0]
    height = im.size[1]
    rate = percent / 100
    x1 = randint(0, width - int(width * rate))
    y1 = randint(0, height - int(height * rate))
    x2 = x1 + int(width * rate)
    y2 = y1 + int(height * rate)
    box = (x1, y1, x2, y2)
    return im.crop(box)

def fltr(im, mode):
    mode = 'ImageFilter.' + mode.upper()
    try:
        return im.filter(eval(mode))
    except:
        sys.exit("Wrong filter mode")

def color(im, weight):
    im = im.convert("RGB")
    arr = np.array(im)
    arr = (arr + weight) % 256
    im = Image.fromarray(np.uint8(arr))
    # for i in range(im.size[0]): # For each pixel:
    #     for j in range(im.size[1]):
    #         [r,g,b] = im.getpixel((i, j))
    #         r = (r + weight) % 256
    #         g = (g + weight) % 256
    #         b = (b + weight) % 256
    #         value = (r,g,b)
    #         im.putpixel((i, j), value)
    return im

def rgb(im):
    im = im.convert("RGB")
    r, g, b = im.split()
    colors = [r, g, b]
    shuffled_colors = colors
    while shuffled_colors == colors:
        shuffled_colors = sample(colors, len(colors))
    return Image.merge("RGB", tuple(shuffled_colors))

def output(image, name):
    try:
        image.save(name)
    except:
        sys.exit("File error")
    return True

if __name__ == "__main__":
    main()
