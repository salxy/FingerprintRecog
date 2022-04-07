# binarization through adaptive thresholding where threshold is mean of neighborhood and median blur for removing pepper after binarization
def binarization(img):
  binaryImage = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
  binaryImage = cv2.medianBlur(binaryImage,3)
  return binaryImage
