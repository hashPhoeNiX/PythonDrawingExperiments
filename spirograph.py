import util
import math
from PIL import Image, ImageDraw

imageDimensions = (2048,2048)
canvas = Image.new('RGBA', imageDimensions, (0, 0, 0, 255))

painter = ImageDraw.Draw(canvas)

colorWhite = (255,255,255)
colorYellow = (255,255,0)
colorMagenta = (255,0,255)
colorCyan = (0,255,255)
penColor = [colorWhite, colorMagenta, colorCyan]
numSubdivisions = 1080

center = (imageDimensions[0] / 2, imageDimensions[1] / 2)
radius = [512, 256]
ratios = [1.0, 24.0]
startAngle = [0, util.deg_to_rad(5), util.deg_to_rad(10)]

tInc = ratios[0] / numSubdivisions
for j in range(3):
    points = []
    for i in range(numSubdivisions + 1):
        t = i * tInc
        angleRad = t * 2 * math.pi * ratios[0] + startAngle[j]
        point = ( center[0] + radius[0] * math.cos(angleRad),
            center[1] + radius[0] * math.sin(angleRad) )
        angleRad = (-t * 2 * math.pi + startAngle[j]) * (ratios[1] - 1)
        point = ( point[0] + radius[1] * math.cos(angleRad),
            point[1] + radius[1] * math.sin(angleRad) )
        points.append(point)
    painter.line(points, fill=penColor[j], width=2)

#canvas.save(util.get_filename(__file__))
canvas.show()
