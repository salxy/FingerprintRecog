# drawing ellipses on minutiae points
def drawing(y, x, img):
  draw = ImageDraw.Draw(img)
  ellipseSize = 2
  draw.ellipse([(x - ellipseSize, y - ellipseSize), (x + ellipseSize, y + ellipseSize)])
