import cv2
import numpy as np



def isValid(width, height):
    if height > width - 7 and height < width + 7:
        return True

    return False


imgUrl = "dados\\sudoku\\sudoku8.jpg"

imgRef = cv2.imread(imgUrl)
imgFinal = cv2.resize(imgRef, (700,700))

img = cv2.imread(imgUrl, cv2.IMREAD_GRAYSCALE)
image = cv2.resize(img, (700,700))

_, thresh = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    # print(x,y,w,h)

    if w > 580 and h > 580 :
        crop_img = image[y:y+h, x:x+w]

        _, thresh1 = cv2.threshold(crop_img, 240, 255, cv2.THRESH_BINARY)
        contours1, hierarchy1 = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour1 in contours1:
            (x1, y1, w1, h1) = cv2.boundingRect(contour1)
            # print(x1,y1,w1,h1)

            if isValid(h1, w1) :
                crop_img1 = image[y+y1:y+y1+h1, x+x1:x+x1+w1]

                _, thresh2 = cv2.threshold(crop_img1, 125, 255, cv2.THRESH_BINARY_INV)
                contours2, hierarchy2 = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                for contour2 in contours2:
                    (x2, y2, w2, h2) = cv2.boundingRect(contour2)
                    print(x2,y2,w2,h2)

                    if w > 30 and h > 30 :
                        cv2.rectangle(imgFinal, (x+x1+5, y+y1+5),(x+x1+w1-5, y+y1+h1-5), (0, 0, 255), 2)






cv2.imshow("img", imgFinal)
# # cv2.imshow("crop", crop_img)
# # cv2.imshow("thresh", thresh)
# # cv2.imshow("thresh1", thresh1)
cv2.waitKey()

# x=14
# y=14
# h=772
# w=772
# crop_img1 = img[y:y+h, x:x+w]
# crop_img = cv2.cvtColor(crop_img1, cv2.COLOR_BGR2GRAY)

# # laplace = cv2.Laplacian(img,cv2.CV_8U)

# # sobelX = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
# # sobelY = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=5)

# # # Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
# # sobelx64f = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
# # abs_sobel64f = np.absolute(sobelx64f)
# # sobel_64 = np.uint8(abs_sobel64f)

# # Definindo área dos dados - threshDados
# _, thresh = cv2.threshold(crop_img, 240, 255, cv2.THRESH_BINARY)

# # Pegando os contornos dos dados das áreas dos dados
# contours, hierarchy = cv2.findContours(
#     thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Acessando todas as formas encontradas na imagem
# for contour in contours:
#     (x, y, w, h) = cv2.boundingRect(contour)

#     print(x,y,w,h)
#     cv2.rectangle(img, (x, y),(x+w, y+h), (0, 0, 255), 1)


# cv2.imshow("img", img)
# cv2.imshow("thresh", thresh)
# cv2.waitKey()

# # cv2.imshow('Original', img)
# # cv2.imshow('Laplace', laplace)
# # cv2.imshow('SobelX',  sobelX)
# # cv2.imshow('SobelY', sobelY)
# # cv2.imshow('Sobel64', sobel_64)

# # cv2.waitKey()

# # cv2.destroyAllWindows()


