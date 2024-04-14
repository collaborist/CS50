from project import rotate, flip, cropbox, croprand, fltr, color, rgb, output
from PIL import Image, ImageFilter, ImageChops
import sys
import pytest
from random import randint, seed, sample
import numpy as np


def test_rotate():
    im = Image.open('1.jpg')
    res = im.rotate(90)
    print(rotate(im, 90), res)
    assert rotate(im, 90) == res


def test_flip():
    im = Image.open('1.jpg')
    result1 = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    result2 = im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    assert flip(im, 'h') == result1
    assert flip(im, 'v') == result2
    with pytest.raises(SystemExit):
        flip(im, 'bv')
        flip(im, 1234)


def test_cropbox():
    im = Image.open('1.jpg')
    width = im.size[0]
    height = im.size[1]
    box1 = (10, 10, 40, 40)
    box2 = (100, 100, width + 400, height + 400)
    box3 = (10 + width, 10 + height, 40, 40)
    assert cropbox(im, box1) == im.crop(box1)
    with pytest.raises(SystemExit):
        cropbox(im, box2)
        cropbox(im, box3)


def test_croprand():
    im = Image.open('1.jpg')
    width = im.size[0]
    height = im.size[1]
    rate = 75 / 100
    seed(0)
    x1 = randint(0, width - int(width * rate))
    y1 = randint(0, height - int(height * rate))
    x2 = x1 + int(width * rate)
    y2 = y1 + int(height * rate)
    box = (x1, y1, x2, y2)
    result = im.crop(box)
    seed(0)
    diff = ImageChops.difference(croprand(im, 75), result)
    assert not diff.getbbox()


def test_fltr():
    im = Image.open('1.jpg')
    assert fltr(im, 'BLUR') == im.filter(ImageFilter.BLUR)
    with pytest.raises(SystemExit):
        fltr(im, 'ImageFilter.hello')
        fltr(im, 'BLURIUS')


def test_color():
    dec = np.ones((11, 11)) * 10
    newim = Image.fromarray(np.uint8(dec))
    test = color(newim, 10)
    train = np.ones((11, 11)) * 20
    train = Image.fromarray(np.uint8(train))
    train = train.convert("RGB")
    diff = ImageChops.difference(test, train)
    assert not diff.getbbox()


def test_rgb():
    seed(0)
    im = Image.open('1.jpg')
    im = im.convert("RGB")
    r, g, b = im.split()
    colors = [r, g, b]
    shuffled_colors = colors
    while shuffled_colors == colors:
        shuffled_colors = sample(colors, len(colors))
    train = Image.merge("RGB", tuple(shuffled_colors))
    diff = ImageChops.difference(rgb(im), train)
    assert not diff.getbbox()


def test_output():
    im = Image.open('1.jpg')
    assert output(im, '2.jpg') == True
    with pytest.raises(SystemExit):
        output(1234, '2.jpg')
