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
