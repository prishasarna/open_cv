import cv2
img=cv2.imread('tiger.jpg')
rotated_90= cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Original Image ', img)
cv2.imshow('Rotated image90 clockwise', rotated_90)
rotated_counter_90= cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('Rotated image90 counterclockwise', rotated_counter_90)
rotated_180= cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow('Rotated image180 clockwise', rotated_180)

cv2.waitKey(0)
cv2.destroyAllWindows()