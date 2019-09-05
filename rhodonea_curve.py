import util
import math
from PIL import Image, ImageDraw

imageDimensions = (2048,2048)
canvas = Image.new('RGBA', imageDimensions, (0, 0, 0, 255))

painter = ImageDraw.Draw(canvas)

center = (imageDimensions[0] / 2, imageDimensions[1] / 2)

radius = 1024
kNum = 7
kDen = 13
kDenReduced = int(kDen / util.gcd(kNum, kDen))
maxAngleRad = math.pi * kDenReduced
numSubdivisions = 180 * kDenReduced
angleRadInc = maxAngleRad / numSubdivisions
points = []
colors = util.color_gradient(numSubdivisions)

for t in range(numSubdivisions):
    angleRad = t * angleRadInc
    r = radius * math.cos(kNum / kDen * angleRad)
    x = center[0] + r * math.cos(angleRad)
    y = center[1] + r * math.sin(angleRad)
    points.append((x, y))

for i in range(numSubdivisions - 1):
    painter.line([points[i], points[i+1]], fill=colors[i], width=2)

#canvas.save("out/" + util.get_filename(__file__))
canvas.show()
