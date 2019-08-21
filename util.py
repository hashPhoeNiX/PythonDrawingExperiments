import os
import math

def cos(angleDeg):
    return math.cos(angleDeg * math.pi / 180)

def sin(angleDeg):
    return math.sin(angleDeg * math.pi / 180)

def getFilename(path):
    return os.path.splitext(os.path.basename(path))[0] + ".png"
