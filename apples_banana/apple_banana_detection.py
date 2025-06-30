import cv2
import numpy as np

img1 =cv2.imread('apple1.jpg',0)
img2 =cv2.imread('apple2.jpg',0)
img3 =cv2.imread('apple3.jpg',0)
img4 =cv2.imread('apple4.jpg',0)
img5 =cv2.imread('banana1.jpg',0)
img6=cv2.imread('banana2.jpg',0)
img7=cv2.imread('banana3.jpg',0)
test=cv2.imread('banana4.jpg',0)
#combine all images into one array
train =np.concatenate((img1,img2,img3,img4,img5,img6,img7),axis=0)
train=train.reshape(-1,10000).astype(np.float32)
test=test.reshape(-1,10000).astype(np.float32)
#label for training and testing, apple=0 and banana=1