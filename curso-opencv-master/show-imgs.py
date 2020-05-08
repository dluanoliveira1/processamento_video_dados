import glob
import cv2

def index_image(index, index_2, op):
    if(op == 1):
        if index >= index_2:
            index = 0
        else:
            index += 1
        return index

    elif(op == 0):
        if index <= 0:
            index = index_2
        else:
            index -= 1
        return index

def resize (width, height):
    dim = (width, height)
    print(dim)
    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

def edited (image):
    # borda
    image = cv2.copyMakeBorder(image, 40, 10, 10, 10, cv2.BORDER_ISOLATED, None, value=[255,255,255])
    
    # texto
    textsize = cv2.getTextSize("Imagem: "+i, cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, 2)[0] 
    image = cv2.putText(image, "Imagem: "+i, (20, 25), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.75, (0, 0, 0), 2, cv2.LINE_AA) 

    # marca d'agua
    watermark = image.copy();
    height, width = image.shape[:2]
    watermark = cv2.putText(watermark, "Paraiba", (width-150, height-50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.75, (0, 0, 0), 2, cv2.LINE_AA)
    image = cv2.addWeighted(watermark, 0.4, image, 0.6, 0)

    return image

list_images = glob.glob('C:\\imgs\\*')
imageslist = []

for i in list_images:

    # tamanho da imagem 512x512
    image = cv2.imread(i)
    print(i)
    image = resize(512,512)
    cv2.imshow('Img',image)
    
    # editando a imagem
    image = edited(image)

    # lista de imagem editada
    imageslist.append(image)
    
index = 0
index_2 = len(imageslist) - 1

# slides
while(1):
    alpha = 1
    beta = 0
    
    src1 = imageslist[index]
    next_index_image = index_image(index, index_2, 1)
    src2 = imageslist[next_index_image]

    # efeito da transição
    for i in range(10):
        new_next_img = cv2.addWeighted(src1, alpha, src2, beta, 0)
        new_current_img = new_next_img
        cv2.imshow('Img', new_current_img)

        # transição alterando alpha e beta
        keycodes = cv2.waitKeyEx(5000)
        if keycodes == -1:
            alpha -= 0.3
            beta += 0.3
        else:
            break
    # teclado
    if keycodes in [ord('q'), ord('Q')]:
        break
    elif keycodes == 2555904:
        index = index_image(index, index_2, 1)
    elif keycodes == 2424832:
        index = index_image(index, index_2, 0)
    else:
        index = index_image(index, index_2, 1)
    

cv2.destroyAllWindows()