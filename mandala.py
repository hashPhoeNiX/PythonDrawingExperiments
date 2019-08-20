import os
import math
from PIL import Image, ImageDraw

def cos(angleDeg):
    return math.cos(angleDeg * math.pi / 180)

def sin(angleDeg):
    return math.sin(angleDeg * math.pi / 180)

imageDimensions = (2048,2048)
canvas = Image.new('RGBA', imageDimensions, (0, 0, 0, 0))

painter = ImageDraw.Draw(canvas)

center = (imageDimensions[0] / 2, imageDimensions[1] / 2)
radius = 1000
colorWhite = (255,255,255)
colorBlack = (0,0,0)
for angle in range(0, 360, 5):
    points = []
    points.append(center[0] + radius * cos(angle + 0))
    points.append(center[1] + radius * sin(angle + 0))
    points.append(center[0] + radius * cos(angle + 120))
    points.append(center[1] + radius * sin(angle + 120))
    points.append(center[0] + radius * cos(angle + 240))
    points.append(center[1] + radius * sin(angle + 240))
    radius -= 1024 * 5 / 360
    color = colorBlack
    if angle % 2 == 1:
        color = colorWhite
    painter.polygon(points, fill=color, outline=colorWhite)

filename = os.path.splitext(os.path.basename(__file__))[0] + ".png"
canvas.save(filename)
#canvas.show()
