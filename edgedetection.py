#cani edge detection:- detect edge
#blurring:- removing noise from the image, smoothem the image, reduction of pixel size
#Types/ Techniques:- Averaging, Gaussion Blur, Median Blur, Bilateral Filtering
import cv2
image =cv2.imread('tiger.jpg')
cv2.imshow('Tiger image', image)
#average(blurs the entire image uniformally)
#blurred1=cv2.blur(image,(3,3))
#cv2.imshow('Blurred Tiger image',blurred1)
#Gaussian blur(focuses on the image and blurs the background)
gaussian_blur =cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('Gaussian Blur',gaussian_blur)
'''#median blur
median_blur=cv2.medianBlur(image,5)
cv2.imshow('Median blur',median_blur)
#Bilateral filter:-considers both spatial and pixel intensity differences
bilateral_blur=cv2.bilateralFilter(image,9,75,75)
cv2.imshow('Bilateral Blur',bilateral_blur)'''
edges=cv2.Canny(gaussian_blur,100,200)
cv2.imshow('Edge',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()



