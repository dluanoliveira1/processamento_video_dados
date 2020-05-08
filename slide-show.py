import numpy as np
import cv2
from PIL import Image, ImageOps
import glob

def getIluminacaoImg(img):
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    channels = [0]
    histSize = [256]
    ranges = [0, 255]

    hist = cv2.calcHist([img_yuv], channels, None, histSize, ranges)

    escuro = np.sum(hist[0:85])
    normal = np.sum(hist[85:170])
    claro = np.sum(hist[170:256])

    maior = max([escuro, normal, claro])

    if maior == escuro:
        return 'Escuro'
    elif maior == normal:
        return 'Normal'
    elif maior == claro:
        return 'Claro'

def modImage (image):
    image = cv2.resize(image,(512,512)) ### Resize
    image = cv2.copyMakeBorder(image, 40, 10, 10, 10, cv2.BORDER_ISOLATED, None, value=[255,255,255]) ### Border
    cv2.putText(image, name + " - " + getIluminacaoImg(image), (20, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 0, 0), 2, cv2.LINE_AA) ### Image Name
    cv2.putText(image, "DLO", (450, 510), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (255, 255, 255), 2, cv2.LINE_AA) ### WM
    return image

image_list = []
image_list_name = []

for item in glob.glob('C:\\imgs\\*'):
    image_list_name.append(item.replace("C:\\imgs\\", ""))
    image_list.append(item)

index = 0
indexNt = 1 
aux = 0
while(1):
    index = index % (len(image_list))
    indexNt = indexNt % (len(image_list))

    image = cv2.imread(image_list[index])
    imageNt = cv2.imread(image_list[indexNt])
    name = image_list_name[index]

    image = modImage(image)
    imageNt = modImage(imageNt)
    # for k in range(0,50):
    #     image[:,:] = np.where(image[:,:]* 1.03 < 255, (image[:,:] * 1.03).astype(np.uint8) , image[:,:])
    #     cv2.imshow('Image',image)
    #     cv2.waitKeyEx(10)
    cv2.imshow('Image',imageNt)
    
    index += 1
    indexNt += 1
    if (cv2.waitKeyEx(4500) == 113):
        break

cv2.destroyAllWindows()
