import util
import math
from PIL import Image, ImageDraw

imageDimensions = (1920,1080)
canvas = Image.new('RGBA', imageDimensions, (0, 0, 0, 255))

painter = ImageDraw.Draw(canvas)

center = (imageDimensions[0] / 2, imageDimensions[1] / 2)

radius = [150, 140]
rho = int( math.fabs(radius[1]) / math.gcd( radius[0], int( math.fabs(radius[1]) ) ) )
maxAngleRad = 2 * math.pi * rho
numSubdivisions = 120 * rho
angleRadInc = maxAngleRad / numSubdivisions
points = []
colors = util.color_gradient(numSubdivisions)

for t in range(numSubdivisions + 1):
    angleRad = t * angleRadInc
    x = center[0]
    y = center[1]
    x += (radius[0] + radius[1]) * math.cos(angleRad)
    y += (radius[0] + radius[1]) * math.sin(angleRad)
    x += radius[1] * math.cos((radius[0] + radius[1]) / radius[1] * angleRad)
    y += radius[1] * math.sin((radius[0] + radius[1]) / radius[1] * angleRad)
    points.append((x, y))

print("Number of points: %d" % len(points))
for i in range(len(points) - 1):
    painter.line([points[i], points[i+1]], fill=colors[i], width=2)
    canvas.save("out/%(frame)06d.png" % {"frame":i})

#canvas.save("out/" + util.get_filename(__file__))
#canvas.show()
