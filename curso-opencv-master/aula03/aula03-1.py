import cv2

img = cv2.imread('C:\\imgs\\lena.jpg')
cv2.imshow('Img',img)

print('Shape: ', img.shape)
print('Size: ' , img.size)
print('Type: ' , img.dtype)

cv2.waitKey()

cv2.destroyAllWindows()


image_list_name.append(filename.replace("C:\\imgs\\", ""))

index = 1
while(1):
    index = index % len(image_list)
    cv2.imshow('Img', np.array(image_list[index]))
    print(image)
    if (cv2.waitKeyEx(5000) == 113):
        break
    index += 1
    
cv2.destroyAllWindows()

