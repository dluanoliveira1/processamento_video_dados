import cv2
import numpy as np

def defineBlobs(img, gray_image):
    #binary image
    _,thresh = cv2.threshold(gray_image, 250, 255,cv2.THRESH_BINARY_INV)
    _,thresh1 = cv2.threshold(gray_image, 50, 255,cv2.THRESH_BINARY_INV)

    #get contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours1, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    height, width = gray_image.shape
    count = 0
    tam = 0
    tam1 = 0

    # computes the bounding box for the contour, and draws it on the frame,
    for contour in contours :
        (x,y,w,h) = cv2.boundingRect(contour)

        if h > 15 :
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 1)
            rx = range((x), (x+w))
            ry = range((y), (y+h))

            for contour1 in contours1 :
                (x1,y1,w1,h1) = cv2.boundingRect(contour1)

                if h1 > 5 and x1 in rx and y1 in ry:
                    cv2.rectangle(img, (x1,y1), (x1+w1,y1+h1), (0,0,255), 1)
                    count = count + 1
            
            cv2.putText(img, str(count), ((x + np.int(w/2) - 12), (y + np.int(h/2) + 5)) , cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, (255, 0, 0), 1, cv2.LINE_AA)
            count = 0

    ##cv2.imshow("Thresh ", thresh)
    cv2.imshow("img",  img)
    cv2.waitKey(0)

###################

img = cv2.imread("img.jpg", cv2.IMREAD_COLOR)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

defineBlobs(img, gray_image)


# def defineBlobs(img, gray_image):
#     #binary image
#     _,thresh = cv2.threshold(gray_image, 255, 255, cv2.THRESH_BINARY)
#     # _,thresh1 = cv2.threshold(gray_image, 50, 255, cv2.THRESH_TOZERO_INV)
#     _,thresh1 = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)

#     #get contours
#     contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     contours1, hierarchy1 = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     height, width = gray_image.shape
#     count = 0
#     tam = 0
#     tam1 = 0

#     # computes the bounding box for the contour, and draws it on the frame,
#     for contour in contours :
#         (x,y,w,h) = cv2.boundingRect(contour)

#         print (x, y, w, h)
        
#         if h > 20 and h < 150 and w - h < 20 :
#             cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 1)
#             crop_img1 = img[y:y+h, x:x+w]
#             crop_img = cv2.cvtColor(crop_img1, cv2.COLOR_BGR2GRAY)
            

#             _,thresh2 = cv2.threshold(crop_img, 150, 255, cv2.THRESH_BINARY_INV)
#             contours2, hierarchy2 = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#             # cv2.imshow("Thresh", thresh2)
#             # cv2.imshow("cropped", crop_img)
#             # cv2.waitKey(0)

#             cutSizeX = 0
#             cutSizeY = 0
#             countSize = 1

#             for contour2 in contours2 :
#                 (x2,y2,w2,h2) = cv2.boundingRect(contour2)
                
#                 cutSizeX = (cutSizeX + w2) / countSize 
#                 cutSizeY = (cutSizeX + h2) / countSize

#                 countSize += 1

#             for contour2 in contours2 :
#                 (x2,y2,w2,h2) = cv2.boundingRect(contour2)

#                 if w2 > cutSizeX - 10 and w2 < cutSizeX + 10 and h2 > cutSizeX - 10 and h2 < cutSizeX + 10 :
#                     # print(x2, y2, w2, h2)
#                     cv2.rectangle(img, (x2 + x,y2 + y), (x2+w2+x,y2+h2+y), (255,0,100), 1)
                
            
#             # rx = range((x), (x+w))
#             # ry = range((y), (y+h))

#             # for contour1 in contours1 :
#             #     (x1,y1,w1,h1) = cv2.boundingRect(contour1)

#             #     cv2.rectangle(img, (x1,y1), (x1+w1,y1+h1), (255,0,255), 1)
#             #     if h1 > 1 and x1 in rx and y1 in ry:
#             #         count = count + 1
            
#             # cv2.putText(img, str(count), ((x + np.int(w/2) - 12), (y + np.int(h/2) + 5)) , cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, (255, 0, 0), 1, cv2.LINE_AA)
#             # count = 0

#     cv2.imshow("Thresh", thresh1)
#     cv2.imshow("img",  img)
#     cv2.waitKey(0)

###################
# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lower_white = np.array([360, 0, 97])
    # upper_white = np.array([340, 0, 95])
    # mask = cv2.inRange(hsv, lower_white, upper_white)

# img = cv2.imread("dados-1.png", cv2.IMREAD_COLOR)
# gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# defineBlobs(img, gray_image)

############################


 

