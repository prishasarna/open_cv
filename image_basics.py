import cv2
image = cv2.imread('tiger.jpg')
image= cv2.resize(image,(600,600))
#rectangle
#cv2.rectangle(image , (100,100), (400,300),(120,120,255), thickness=-2)
# convert to greyscale
grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.putText(image,"Hello this is a Tiger ",(200,200),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,3,(0,0,0),2)
cv2.imshow('Tiger Image', image)
cv2.imshow('Grey scaled Image',grey_image)
print(image.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
