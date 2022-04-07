# matching 2 images' minutiae points to figure out if the fingerprints belong to the same person
def matchingScore(featuresA, featuresB, tolerance=10):
  countMatching= 0
  if(len(featuresA) < len(featuresB)):
    size = len(featuresA)
  else:
    size = len(featuresB)
  avgMinutiae = (len(featuresA) + len(featuresB))/2
  for k in range(0, size):
    spatialDistance = calculateDistance(featuresA[k][0], featuresA[k][1], featuresB[k][0], featuresB[k][1])
    if(spatialDistance <= tolerance):
      countMatching +=1
  matchingPerc = countMatching/avgMinutiae*100
  return matchingPerc
