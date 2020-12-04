#!/usr/bin/env python3

import matelight
import time
import random

x1=0
x2=0
x3=0
x4=0
x5=0
y1=0
y2=0
y3=0
y5=0
y4=0
x6=0
x7=0
x8=0
x9=0
x10=0
y6=0
y7=0
y8=0
y9=0
y10=0
yx=0
rc3_primary_colors = [
        ["#b239ff", "#670295", "#440069", "#240038"],
        ["#6800e7", "#41008b", "#2a005e", "#14002f"],
        ["#05b9ec", "#0076a9", "#025d84", "#002a3a"],
    ]

def hex2rgb(color):
    color = color[1:]
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

def rc3_xmastree(ml):
    for y in range(ml.height):
        for x in range(ml.width):
            # i = random.randint(len(rc3_primary_colors))
            # color = random.choice(rc3_primary_colors[i])
            #color = random.choice(random.choice(rc3_primary_colors))
            ml.set_pixel(x, y, *hex2rgb("#000000"))
    ml.show()
    
    wh=0
    colorv="#01A08F"
    for x in [7]:
        ml.set_pixel(x, 2, *hex2rgb(colorv))
    for x in range(6, 9):
        ml.set_pixel(x, 3, *hex2rgb(colorv))
    for x in range(5,10):
        ml.set_pixel(x, 4, *hex2rgb(colorv))
    for x in range(4,11):
        ml.set_pixel(x, 5, *hex2rgb(colorv))
    for x in range(5,10):
        ml.set_pixel(x, 6, *hex2rgb(colorv))
    for x in range(3,12):
        ml.set_pixel(x, 7, *hex2rgb(colorv))
    for x in range(4,11):
        ml.set_pixel(x, 8, *hex2rgb(colorv))
    for x in range(2,13):
        ml.set_pixel(x, 9, *hex2rgb(colorv))
    for x in range(3,12):
        ml.set_pixel(x, 10, *hex2rgb(colorv))
    for x in range(1,14):
        ml.set_pixel(x, 11, *hex2rgb(colorv))
    for x in range(2,13):
        ml.set_pixel(x, 12, *hex2rgb(colorv))
    for x in range(0,15):
        ml.set_pixel(x, 13, *hex2rgb(colorv))
    for x in range(6,9):
        ml.set_pixel(x, 14, *hex2rgb(colorv))
    for x in range(6,9):
        ml.set_pixel(x, 15, *hex2rgb(colorv))
    ml.show() 
        
    while wh < 20:
        x1 = random.randint(4,10)
        y1 = 5
        x2 = random.randint(3,11)
        y2 = 7
        x3 = random.randint(2,12)
        y3 = 9
        x4 = random.randint(1,13)
        y4 = 11
        x5 = random.randint(0,14)
        y5 = 13
        x6 = random.randint(5,9)
        y6 = 6
        x7 = random.randint(4,10)
        y7 = 8
        x8 = random.randint(3,11)
        y8 = 10
        x9 = random.randint(2,12)
        y9 = 12
        x10 = random.randint(6,8)
        y10 = 3
        colorg="#FFF900"
        colorr="#FD294F"
 #       color1 = random.choice(random.choice(rc3_primary_colors))
 #       color2 = random.choice(random.choice(rc3_primary_colors))
#        color3 = random.choice(random.choice(rc3_primary_colors))
#        color4 = random.choice(random.choice(rc3_primary_colors))
        ml.set_pixel(x1, y1, *hex2rgb(colorg))
        ml.set_pixel(x2, y2, *hex2rgb(colorg))
        ml.set_pixel(x3, y3, *hex2rgb(colorg))
        ml.set_pixel(x4, y4, *hex2rgb(colorg))
        ml.set_pixel(x5, y5, *hex2rgb(colorg))
        ml.set_pixel(x6, y6, *hex2rgb(colorr))
        ml.set_pixel(x7, y7, *hex2rgb(colorr))
        ml.set_pixel(x8, y8, *hex2rgb(colorr))
        ml.set_pixel(x9, y9, *hex2rgb(colorr))
        ml.set_pixel(x10, y10, *hex2rgb(colorr))

        ml.show()
        time.sleep(3)
        ml.set_pixel(x1, y1, *hex2rgb(colorv))
        ml.set_pixel(x2, y2, *hex2rgb(colorv))
        ml.set_pixel(x3, y3, *hex2rgb(colorv))
        ml.set_pixel(x4, y4, *hex2rgb(colorv))
        ml.set_pixel(x5, y5, *hex2rgb(colorv))
        ml.set_pixel(x6, y6, *hex2rgb(colorv))
        ml.set_pixel(x7, y7, *hex2rgb(colorv))
        ml.set_pixel(x8, y8, *hex2rgb(colorv))
        ml.set_pixel(x9, y9, *hex2rgb(colorv))
        ml.set_pixel(x10, y10, *hex2rgb(colorv))
        ml.show()
        wh=wh+1


if __name__ == "__main__":
    ml = matelight.Matelight(3, 4, serial="window/canvas")
    ml.clear()

    # while True:
    if True:
        effect = random.randint(1, 9)
        effect = 0
    # for effect in range(6):
        if effect == 0:
            rc3_xmastree(ml)
        # ml.clear()
