import cv2
import numpy as np
img1 = cv2.imread('apple1.jpg',0)
img2 = cv2.imread('apple2.jpg',0)
img3 = cv2.imread('apple3.jpg',0)

img4 = cv2.imread('banana1.jpg',0)
img5 = cv2.imread('banana2.jpg',0)
img6 = cv2.imread('banana3.jpg',0)

test = cv2.imread('banana5.jpg',0)

# Combine the images into one array
train = np.concatenate((img1, img2, img3, img4, img5, img6), axis=0)

# Prepare train and test datasets
train = train.reshape(-1,10000).astype(np.float32)
test = test.reshape(-1,10000).astype(np.float32)
#create labels for train /test,Apple->0 and Banana->1
train_labels = np.array([[0],[0],[0],[1],[1],[1]]).astype(np.float32)
knn = cv2.ml.KNearest_create()
knn.train(train,cv2.ml.ROW_SAMPLE,train_labels)
ret,result,neighbors,dist = knn.findNearest(test,k=1)

if result==0:
    print("This would be Apple")
elif result==1:
    print("This would be Banana")
