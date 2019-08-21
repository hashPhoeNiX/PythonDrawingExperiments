import util
import math
from PIL import Image, ImageDraw

def subdivideSegment(startPoint, endPoint, numSubdivisions):
    vec = [endPoint[0] - startPoint[0], endPoint[1] - startPoint[1]]
    vec[0] /= numSubdivisions
    vec[1] /= numSubdivisions
    points = []
    for t in range(numSubdivisions + 1):
        point = (startPoint[0] + vec[0] * t, startPoint[1] + vec[1] * t)
        points.append(point)
    return points

def drawLines(pointsA, pointsB, painter, color=(255, 255, 255)):
    numPoints = len(pointsA) if len(pointsA) < len(pointsB) else len(pointsB)
    for i in range(numPoints):
        painter.line([pointsA[i], pointsB[i]], fill=color, width=1)

imageDimensions = (2048,2048)
canvas = Image.new('RGBA', imageDimensions, (0, 0, 0, 255))

painter = ImageDraw.Draw(canvas)

colorWhite = (255,255,255)
numSubdivisions = 32

diag = subdivideSegment((2048, 2048), (0, 0), numSubdivisions)

upEdge = subdivideSegment((0, 0), (2048, 0), numSubdivisions)
dnEdge = subdivideSegment((0, 2048), (2048, 2048), numSubdivisions)

drawLines(diag, upEdge, painter, colorWhite)
drawLines(diag, dnEdge, painter, colorWhite)

canvas.save(util.getFilename(__file__))
canvas.show()
