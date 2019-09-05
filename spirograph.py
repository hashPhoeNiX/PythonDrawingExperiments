import util
import math
from PIL import Image, ImageDraw

imageDimensions = (2048,2048)
numSubdivisions = 1080

center = (imageDimensions[0] / 2, imageDimensions[1] / 2)
radius = [512, 256]

start = 1
end = 21

for j in range(start, end):
    for k in range(j, end):
        if util.gcd(j, k - 1) != 1:
            continue

        canvas = Image.new('RGBA', imageDimensions, (0, 0, 0, 255))
        painter = ImageDraw.Draw(canvas)

        ratios = [j, k]
        tInc = 1 / numSubdivisions
        points = []
        for i in range(numSubdivisions + 1):
            t = i * tInc
            angleRad = t * 2 * math.pi * ratios[0]
            point = ( center[0] + radius[0] * math.cos(angleRad),
                center[1] + radius[0] * math.sin(angleRad) )
            angleRad = (-t * 2 * math.pi) * (ratios[1] - 1)
            point = ( point[0] + radius[1] * math.cos(angleRad),
                point[1] + radius[1] * math.sin(angleRad) )
            points.append(point)

        colors = util.color_gradient(numSubdivisions)
        for i in range(numSubdivisions):
            painter.line([points[i], points[i+1]], fill=colors[i], width=2)

        canvas.save( "out/spirograph_%(ratio1)02d-%(ratio2)02d.png" %
            {"ratio1":ratios[0], "ratio2":ratios[1]} )
