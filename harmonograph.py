import util
import math
from PIL import Image, ImageDraw

imageDimensions = (1920,1080)
canvas = Image.new('RGBA', imageDimensions, (0, 0, 0, 255))

painter = ImageDraw.Draw(canvas)

center = (imageDimensions[0] / 2, imageDimensions[1] / 2)

points = []
amp = [480, 480, 270, 270]
dampFactor = [.000006, .00001, 0.00001, 0.00001]
freq = [.099, .298, .0995, .3]
phaseDeg = [0, 0, 45, 60]
minThreshold = 0.5

t = 0
while True:
    x = center[0]
    y = center[1]
    numTerms = int(len(amp) / 2)
    terminate = False
    for i in range(numTerms):
        damp = math.exp(-dampFactor[i] * t)
        x += amp[i] * math.sin(util.deg_to_rad(freq[i] * t + phaseDeg[i])) * damp
        if (damp < minThreshold):
            terminate = True
        damp = math.exp(-dampFactor[numTerms + i] * t)
        y += amp[numTerms + i] * math.sin(util.deg_to_rad(freq[numTerms + i] * t + phaseDeg[numTerms + i])) * damp
        if (damp < minThreshold):
            terminate = True
    points.append((x, y))
    t += 8
    if terminate:
        break

print("Number of points: %d" % len(points))
colors = util.color_gradient(len(points) - 1)
for i in range(len(points) - 1):
    painter.line([points[i], points[i+1]], fill=colors[i], width=2)
    #canvas.save("out/harmonograph_%(frame)06d.png" % {"frame":i})

#canvas.save(util.get_filename(__file__))
canvas.show()
