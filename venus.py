#!/usr/bin/env python3

import matelight
import time
import random

rc3_primary_colors = [
        ["#b239ff", "#670295", "#440069", "#240038"],
        ["#6800e7", "#41008b", "#2a005e", "#14002f"],
        ["#05b9ec", "#0076a9", "#025d84", "#002a3a"],
    ]

def hex2rgb(color):
    color = color[1:]
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

def rc3_venus(ml):
    for y in range(ml.height):
        for x in range(ml.width):
            # i = random.randint(len(rc3_primary_colors))
            # color = random.choice(rc3_primary_colors[i])
            #color = random.choice(random.choice(rc3_primary_colors))
            ml.set_pixel(x, y, *hex2rgb("#002a3a"))
    ml.show()
    
    wh=0
    colorv="#b239ff"
    while wh < 20:
        colorv="#b239ff"
        if wh % 2 == 0:
            colorv="#6800E7"
        for x in range(6,9):
            ml.set_pixel(x, 2, *hex2rgb(colorv))
        for x in [5,6,8,9]:
            ml.set_pixel(x, 3, *hex2rgb(colorv))
        for x in [4,5,9,10]:
            ml.set_pixel(x, 4, *hex2rgb(colorv))
        for x in [3,4,10,11]:
            ml.set_pixel(x, 5, *hex2rgb(colorv))
        for x in [3,11]:
            ml.set_pixel(x, 6, *hex2rgb(colorv))
        for x in [3,4,10,11]:
            ml.set_pixel(x, 7, *hex2rgb(colorv))
        for x in [4,5,9,10]:
            ml.set_pixel(x, 8, *hex2rgb(colorv))
        for x in range(5,10):
            ml.set_pixel(x, 9, *hex2rgb(colorv))
        for x in range(7,8):
            ml.set_pixel(x, 10, *hex2rgb(colorv))
        for x in range(7,8):
            ml.set_pixel(x, 11, *hex2rgb(colorv))
        for x in range(5,10):
            ml.set_pixel(x, 12, *hex2rgb(colorv))
        for x in range(7,8):
            ml.set_pixel(x, 13, *hex2rgb(colorv))
        for x in range(7,8):
            ml.set_pixel(x, 14, *hex2rgb(colorv))
        wh=wh+1
        time.sleep(1)
        ml.show() 


if __name__ == "__main__":
    ml = matelight.Matelight(3, 4, serial="window/canvas")
    ml.clear()

    # while True:
    if True:
        effect = random.randint(1, 9)
        effect = 0
    # for effect in range(6):
        if effect == 0:
            rc3_venus(ml)
        # ml.clear()
