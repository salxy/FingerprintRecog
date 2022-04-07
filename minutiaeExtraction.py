# extracting minutiae points from given image and returning them in a dictionary of lists
def extraction(img):
  image2 = img_as_float(img)
  row, col = image2.shape
  features = {"bifurcation":[],"ending":[]}
  arrFeatures = []
  cn1 = 0
  cn3 = 0
  for i in range(1, row - 1):
    for j in range(1, col - 1):
      minutiaeType = computation(image2, i, j)
      if minutiaeType == "ending":
        cn1 += 1
        features[minutiaeType].append((i,j))
        arrFeatures.append((i, j))
        drawing(i, j, img)
      elif minutiaeType == "bifurcation":
        cn3 += 1
        features[minutiaeType].append((i,j))
        arrFeatures.append((i, j))
        drawing(i, j, img)
  return img, cn1, cn3, features, arrFeatures
