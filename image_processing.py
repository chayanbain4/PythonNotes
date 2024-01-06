# from PIL import Image #pip install Pillow

# #How to open and show an Image?

# # image = Image.open("image.jpg")
# # image.show()

# #How to transpose an Image?


# image = Image.open("image.jpg")

# # transposed_img = image.transpose(Image.FLIP_LEFT_RIGHT) #Horizontal
# transposed_img1 = image.transpose(Image.FLIP_TOP_BOTTOM) #Vertically
# # transposed_img.save('correct.jpg')
# transposed_img1.save('correct1.jpg')

# print("Done Flipping")


# import cv2 #pip ibstall opencv-python

# img = cv2.imread('boat.jpg') #opened image

# # Histogram equalization (CLAHE)
# clahe = cv2.createCLAHE()

# #covert colorful image to B&W
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #apply enhancement
# enh_img = clahe.apply(gray_img)

# #save the file
# cv2.imwrite('enhanced2.jpg', enh_img)

# print("Done enhancing")






















import cv2

#Image smoothning

# img = cv2.imread('boat.jpg', 1)
# img = cv2.resize(img, (300,300)) #Crop
# # Apply blur
# img1 = cv2.blur(img,(3,3))
# # display the images
# cv2.imshow('Original', img)
# cv2.imshow('Blur', img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# #Blur processing

# img = cv2.imread('boat.jpg', 1)
# img = cv2.resize(img, (320,210))
# # Apply Gaussian blur
# img1 = cv2.GaussianBlur(img,(5,5),2)
# # display the images
# cv2.imshow('Original', img)
# cv2.imshow('Gaussian', img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#Edge ditection ()

import numpy as np
# img = cv2.imread('image.jpg', 0)
# img = cv2.resize(img, (300,200))
# # Laplacian image gradient
# lap = np.uint8(np.absolute(cv2.Laplacian(img,cv2.CV_64F, ksize=1)))
# # display the images
# cv2.imshow('Original', img)
# cv2.imshow('Lpalacian', lap)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 

#---------------------------------------------------------------------------------------

# img = cv2.imread('image.jpg', 0)
# img = cv2.resize(img, (370,400))
# # Sobel image gradient
# vertical = np.uint8(np.absolute(cv2.Sobel(img,cv2.CV_64F, 1,0, ksize=1)))
# horizon = np.uint8(np.absolute(cv2.Sobel(img,cv2.CV_64F, 0,1, ksize=1)))
# # display the images
# cv2.imshow('Vertical', vertical)
# cv2.imshow('Horizontal', horizon)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# canny edge detection

# img = cv2.imread('image.jpg', 0)
# def null(x):
#     pass
# # create trackbars to control threshold values
# cv2.namedWindow('Canny')
# cv2.createTrackbar('MIN', 'Canny', 80,255, null)
# cv2.createTrackbar('MAX', 'Canny', 120,255, null)
# while True:
#     # get Trackbar position
#     a = cv2.getTrackbarPos('MIN', 'Canny')
#     b = cv2.getTrackbarPos('MAX', 'Canny')
#     # Canny Edge detection
#     # arguments: image, min_val, max_val
#     canny = cv2.Canny(img,a,b)
#     # display the images
#     cv2.imshow('Canny', canny)
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('q'):
#         break
# cv2.destroyAllWindows() 




#Adapting Threshold of an Image

# img = cv2.imread('boat.jpg', 0)
# img = cv2.resize(img, (320,225))
# # apply various adaptive thresholds
# th1 = cv2.adaptiveThreshold(img, 255, \
#                                 cv2.ADAPTIVE_THRESH_MEAN_C, \
#                                 cv2.THRESH_BINARY, 7, 4)
# th2 = cv2.adaptiveThreshold(img, 255, \
#                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
#                                 cv2.THRESH_BINARY, 7, 4)
# # display the images
# cv2.imshow('ADAPTIVE_THRESHOLD_MEAN', th1)
# cv2.imshow('ADAPTIVE_THRESHOLD_GAUSSIAN', th2)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 



#Thresholding an Image

# read an image in grayscale
# img = cv2.imread('boat.jpg', 0)
# img = cv2.resize(img, (320,225))
# # apply various thresholds
# val, th1 = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
# val, th2 = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY_INV)
# val, th3 = cv2.threshold(img, 110, 255, cv2.THRESH_TRUNC)
# val, th4 = cv2.threshold(img, 110, 255, cv2.THRESH_TOZERO)
# val, th5 = cv2.threshold(img, 110, 255, cv2.THRESH_TOZERO_INV)
# # display the images
# cv2.imshow('Original', img)
# cv2.imshow('THRESH_BINARY', th1)
# cv2.imshow('THRESH_BINARY_INV', th2)
# cv2.imshow('THRESH_TRUNC', th3)
# cv2.imshow('THRESH_TOZERO', th4)
# cv2.imshow('THRESH_TOZERO_INV', th5)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 