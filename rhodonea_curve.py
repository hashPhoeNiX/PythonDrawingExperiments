import util
import math
from PIL import Image, ImageDraw

imageDimensions = (1920,1080)
canvas = Image.new('RGBA', imageDimensions, (0, 0, 0, 255))

painter = ImageDraw.Draw(canvas)

center = (imageDimensions[0] / 2, imageDimensions[1] / 2)

radius = 270
kNum = 3
kDen = 1
kDenReduced = int(kDen / util.gcd(kNum, kDen))
maxAngleRad = math.pi * kDenReduced
numSubdivisions = 360 * kDenReduced
angleRadInc = maxAngleRad / numSubdivisions
points = []
colors = util.color_gradient(numSubdivisions)

for t in range(numSubdivisions + 1):
    angleRad = t * angleRadInc
    r = radius * math.cos(kNum / kDen * angleRad)
    x = center[0] + r * math.cos(angleRad)
    y = center[1] + r * math.sin(angleRad)
    points.append((x, y))

print("Number of points: %d" % len(points))
for i in range(len(points) - 1):
    painter.line([points[i], points[i+1]], fill=colors[i], width=2)
    #canvas.save("out/%(frame)06d.png" % {"frame":i})

#canvas.save("out/" + util.get_filename(__file__))
canvas.show()
