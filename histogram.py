# displaying histogram to check how adaptive histogram equalization affects image's histogram
def displayHistogram(img, title):
  hist = cv2.calcHist([img], [0], None, [256], [0, 256])
  plt.figure()
  plt.title(title)
  plt.xlabel("Pixel Value")
  plt.ylabel("# of Pixels")
  plt.plot(hist)
  plt.xlim([0, 256])

# adaptive histogram equalization to improve contrast through stretching out intensity range
def adaptiveHistogramEqualization(img):
  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
  equalizedImage = clahe.apply(img)
  return equalizedImage
