import numpy as np
import cv2
from PIL import Image, ImageOps
import glob

image_list = []
image_list_name = []

for item in glob.glob('C:\\imgs\\*'):
    im = Image.open(item)
    im = im.resize((512, 512), Image.ANTIALIAS)
    im = ImageOps.expand(im, border=(10,40,10,10), fill=(255,255,255))
    image_list_name.append(item.replace("C:\\imgs\\", ""))
    image_list.append(im)

index = 1
while(1):
    index = index % (len(image_list))
    image = np.array(image_list[index])
    name = image_list_name[index]

    height, width = image.shape[:2]
    cv2.putText(image, name, (20, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 0, 0), 2, cv2.LINE_AA) 
    cv2.putText(image, "DLO", (width-75, height-50), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('Img', image)
    
    index += 1
    if (cv2.waitKeyEx(5000) == 113):
        break

cv2.destroyAllWindows()
