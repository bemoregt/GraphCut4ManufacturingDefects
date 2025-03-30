import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('NG(97)(151).png')
img = cv2.imread('NG(98)(91)(1).png')
#img = cv2.imread('NG(99)(51) (1).png')
#img = cv2.imread('NG(99)(449) (1).png')
#img = cv2.imread('NG(99)(442) (1).png')
#img = cv2.imread('NG(99)(47) (1).png')
#img = cv2.imread('NG(99)(48) (1).png')
#img = cv2.imread('NG(99)(452) (1).png')
#img = cv2.imread('NG(99)(2) (1).png')
#img = cv2.imread('NG(99)(2) (1).png')
#img = cv2.imread('NG(99)(624) (1).png')
#img = cv2.imread('NG(99)(765) (1).png')
#img = cv2.imread('NG(99)(803) (1).png')
#img = cv2.imread('NG(99)(713) (1).png')
#img = cv2.imread('NG(99)(588) (1).png')
#img = cv2.imread('NG(99)(452) (1).png')
#img = cv2.imread('NG(99)(437) (1).png')
#img = cv2.imread('NG(99) (1).png')

mask = np.zeros((img.shape[:2]), np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
##rect = (100, 100, 70, 70)
rect = (100, 100, 70, 70)

## #Here calculated 9 times ======================
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 9, cv2.GC_INIT_WITH_RECT)

#About the first parameter of the where function is the condition.
##If the condition is met, the value is 0, otherwise it is 1. If there is only the first parameter, it returns the coordinates of the element that meets the condition.
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

#mask2 is fixed like this
plt.figure(figsize=(19, 9))
plt.subplot(1, 2, 1)
x1 = rect[0]
y1 = rect[1]
x2 = rect[2]
y2 = rect[3]
cv2.rectangle(img, (x1, y1), (x1 + x2, y1 + y2), (255, 0, 0), 1)
plt.imshow(img)
plt.title('original image ')

plt.subplot(1, 2, 2)
#The img here is also fixed.
##img = img * mask2[:, :, np.newaxis]
img = mask2[:, :, np.newaxis]
plt.imshow(img)
plt.title('target image')

plt.show()