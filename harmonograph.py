import util
import math
from PIL import Image, ImageDraw

imageDimensions = (2048,2048)
canvas = Image.new('RGBA', imageDimensions, (0, 0, 0, 255))

painter = ImageDraw.Draw(canvas)

center = (imageDimensions[0] / 2, imageDimensions[1] / 2)

points = []
amp = [768, 768]
ampDamp = [.00006, .00005]
freq = [3, 5]
phaseDeg = [0, 30]
approxZero = 0.5

t = 0
while math.exp(-ampDamp[0] * t) > approxZero and math.exp(-ampDamp[1] * t) > approxZero:
    x = center[0]
    y = center[1]
    x += amp[0] * math.sin(util.deg_to_rad(freq[0] * t + phaseDeg[0])) * math.exp(-ampDamp[0] * t)
    y += amp[1] * math.sin(util.deg_to_rad(freq[1] * t + phaseDeg[1])) * math.exp(-ampDamp[1] * t)
    points.append((x, y))
    t += 1

print(t)
colors = util.color_gradient(t)
for i in range(t - 1):
    painter.line([points[i], points[i+1]], fill=colors[i], width=2)

#canvas.save(util.get_filename(__file__))
canvas.show()
