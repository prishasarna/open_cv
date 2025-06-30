#Implementing a simple KNN system
import cv2
import numpy as np
import matplotlib.pyplot as plt
trainData = np.random.randint(0,100,(20,2)).astype(np.float32)
labels =np.random.randint(0,2,(20,1)).astype(np.float32)
#when label=0,red triangle
red = trainData[labels.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')

#when label=1,blue square
blue = trainData[labels.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

test = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(test[:,0],test[:,1],80,'g','o')
plt.show()
knn=cv2.ml.KNearest_create()
knn.train(trainData,cv2.ml.ROW_SAMPLE,labels)
ret ,results ,neighbors , dist= knn.findNearest(test,3)

print("result : {}\n".format(results))
print("neighbors : {}\n".format(neighbors))
print("distance : {}\n".format(dist))