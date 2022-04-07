import cv2 # main library
from matplotlib import pyplot as plt # to plot histograms
from google.colab.patches import cv2_imshow # to display images in google colab
import numpy as np # to convert images to matrices
from skimage.util import invert # to invert image before thinning
from PIL import Image, ImageDraw # to draw ellipses on image
from skimage import img_as_float # to convert image to array of floats

# creating a dataset of 5 fingerprints
datasetOriginalFingerprints = ['1_2.TIF', '1_3.TIF', '1_4.TIF', '1_5.TIF', '1_6.TIF']
namesOfOwners = ['Mohammad', 'Khaled', 'Salwa', 'Hammoud', 'Chatila']
datasetProcessedFingerprints = {'1_2.TIF':[], '1_3.TIF':[], '1_4.TIF':[], '1_5.TIF':[], '1_6.TIF':[]}

for data in datasetOriginalFingerprints:
  originalImage = cv2.imread(data)
  grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  blurredImage = gauss(grayImage)
  equalizedImage = adaptiveHistogramEqualization(blurredImage)
  binaryImage = binarization(equalizedImage)
  skeletonImage = thinning(binaryImage)
  processedImage, CN1, CN3, features, arrOfFeatures = extraction(skeletonImage)
  datasetProcessedFingerprints[data].append((processedImage, CN1, CN3, features, arrOfFeatures))

'''
datasetProcessedFingerprints['1_2.TIF'][0][0] has the image, 
datasetProcessedFingerprints['1_2.TIF'][0][1] has the number of minutiae points with cn=1
datasetProcessedFingerprints['1_2.TIF'][0][2] has the number of minutiae points with cn=3
datasetProcessedFingerprints['1_2.TIF'][0][3] has a dictionary that contains location of ridge endings and bifurcations
datasetProcessedFingerprints['1_2.TIF'][0][4] has an array of all minutiae points (endings and bifurcations)
'''

# processing testing fingerprint
testingImage = cv2.imread('1_4.TIF')
print("Original Fingerprint:")
cv2_imshow(testingImage)

grayImage = cv2.cvtColor(testingImage, cv2.COLOR_BGR2GRAY)
print("Grayscale Fingerprint:")
cv2_imshow(grayImage)

blurredImage = gauss(grayImage)
equalizedImage = adaptiveHistogramEqualization(blurredImage)
binaryImage = binarization(equalizedImage)
skeletonImage = thinning(binaryImage)
print("Preprocessed Fingerprint:")
display(skeletonImage)

processedImage, CN1, CN3, features, arrOfFeatures = extraction(skeletonImage)
print("Processed Fingerprint:")
display(processedImage)

# comparing testing fingerprint to dataset
counter = 0
for data in datasetOriginalFingerprints:
  arrayOfDatasetImage = datasetProcessedFingerprints[data][0][4]
  score = matchingScore(arrOfFeatures, arrayOfDatasetImage)
  if(score == 100):
    print("\nThe input fingerprint belongs to:", namesOfOwners[counter]) 
    print("File name:", data)
    break
  counter += 1


print("\n\nChange in histogram is shown clearly in the histograms below:")
displayHistogram(blurredImage, "Before Equalization")
displayHistogram(equalizedImage, "After Equalization")
