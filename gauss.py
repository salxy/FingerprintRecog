# gaussian blur with kernel size 7 and variance 0
def gauss(img):
  smoothedImage = cv2.GaussianBlur(img,(7,7), 0)
  return smoothedImage
