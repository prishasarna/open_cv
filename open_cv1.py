# open source computer vision library, images , videos , processing also
# 0-255 where 0 is black and then 255 is white and all colours in between
# greyscale is single channel
# coloured images is (b,g,r)
import cv2
import numpy as np
black_image = np.zeros((512,512,3),dtype=np.uint8)
#rectangle
cv2.rectangle(black_image , (100,100), (400,300),(120,120,255), thickness=-1)
#drawing line
cv2.line(black_image,(0,0),(512,512),(255,56,0),2)
#circle
cv2.circle(black_image,(150,150),75,(0,255,0),-1)
#put text
cv2.putText(black_image,"Hello OpenCV",(100,100),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),2)
cv2.imshow('Black Image',black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

