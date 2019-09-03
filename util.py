import os
import math

def deg_to_rad(angleDeg):
    return angleDeg * math.pi / 180.0

def cos(angleDeg):
    return math.cos(deg_to_rad(angleDeg))

def sin(angleDeg):
    return math.sin(deg_to_rad(angleDeg))

def get_filename(path):
    return os.path.splitext(os.path.basename(path))[0] + ".png"

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if b > a:
        c = b
        b = a
        a = c
    c = a % b
    return gcd(b, c)

def fraction_reduce(numerator, denominator):
    c = gcd(numerator, denominator)
    return [numerator/c, denominator/c]

def swap(a, b):
    return (b, a)

def color_gradient(numSubdivisions):
    colors = []
    angleDegInc = 360 / numSubdivisions
    for i in range(numSubdivisions):
        angleDeg = i * angleDegInc
        if angleDeg <= 60:
            green = int(angleDeg / 60 * 255)
            color = (255, green, 0)
        elif angleDeg <= 120:
            red = int( ( 1 - (angleDeg - 60) / 60 ) * 255 )
            color = (red, 255, 0)
        elif angleDeg <= 180:
            blue = int( (angleDeg - 120) / 60 * 255)
            color = (0, 255, blue)
        elif angleDeg <= 240:
            green = int( ( 1 - (angleDeg - 180) / 60 ) * 255 )
            color = (0, green, 255)
        elif angleDeg <= 300:
            red = int( (angleDeg - 240) / 60 * 255)
            color = (red, 0, 255)
        else: # angleDeg <= 360
            blue = int( ( 1 - (angleDeg - 300) / 60 ) * 255 )
            color = (255, 0, blue)
        colors.append(color)
    return colors
