import util
from PIL import Image, ImageDraw

imageDimensions = (2048,2048)
canvas = Image.new('RGBA', imageDimensions, (0, 0, 0, 0))

painter = ImageDraw.Draw(canvas)

center = (imageDimensions[0] / 2, imageDimensions[1] / 2)
colorWhite = (255,255,255)
colorBlack = (0,0,0)
isEven = True
angleInc = 2
maxAngle = 540
radius = 1000
radiusInc = radius * angleInc / maxAngle

for angle in range(0, maxAngle, angleInc):
    points = []
    points.append(center[0] + radius * util.cos(angle + 0))
    points.append(center[1] + radius * util.sin(angle + 0))
    points.append(center[0] + radius * util.cos(angle + 120))
    points.append(center[1] + radius * util.sin(angle + 120))
    points.append(center[0] + radius * util.cos(angle + 240))
    points.append(center[1] + radius * util.sin(angle + 240))
    radius -= radiusInc
    painter.polygon(points, fill=colorBlack if isEven else colorWhite, outline=colorWhite)
    isEven = not isEven

#canvas.save(util.get_filename(__file__))
canvas.show()
