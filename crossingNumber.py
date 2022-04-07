# computing crossing number to figure out what kind of ridge point said pixel is
def computation(img, i, j):
  cells = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
  if(int(img[i][j]) == 0):
    p = [int(img[i + k][j + l]) for k, l in cells]
    cn = 0
    for k in range(0, 8):
      cn += abs(int(p[k]) - int(p[k + 1]))
    cn *= 0.5
    if cn == 1.0:
      return "ending"
    elif cn == 3.0:
      return "bifurcation"
  return "none"
