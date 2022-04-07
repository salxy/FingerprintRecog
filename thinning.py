# thinning image through transforming binary image into a skeletized form using the technique of Zhang-Suen
def thinning(img):
  thinnedImage = cv2.ximgproc.thinning(invert(img))
  data = np.array(thinnedImage)
  row, col = data.shape
  for i in range(0, row):
    for j in range(0, col):
      if(data[i, j] == 255):
        data[i, j] = 0
      else:
        data[i, j] = 255
  thinnedImage = Image.fromarray(data)
  return thinnedImage
