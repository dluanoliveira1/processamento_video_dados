import cv2
import numpy as np

def isValid(width, height):
    if height > width - 7 and height < width + 7:
        return True
    return False


countingImg = 1
while True:
    # Imagem que será processada
    imgUrl = "dados\\sudoku\\sudoku" + str(countingImg) + ".jpg"

    # Imagem para escrever os resultados finais
    imgRef = cv2.imread(imgUrl)
    imgFinal = cv2.resize(imgRef, (700,700))

    # Imagem para utilizar durante processamento dos quadrados
    img = cv2.imread(imgUrl, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(img, (700,700))

    # Encontrando os boards dentro da imagem
    _, thresh = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        print(x,y,w,h)

        if w > 300 and h > 300 :
            # Cortando os boards existentes para analisar de forma independente
            crop_img_n = image[y:y+h, x:x+w]
            # Aplicando blur para tirar os ruidos que interferem na obtenção dos quadrados
            crop_img = cv2.GaussianBlur(crop_img_n, (5,3), cv2.BORDER_DEFAULT)

            # Encontrando os quadrados dentro do board
            _, thresh1 = cv2.threshold(crop_img, 240, 255, cv2.THRESH_BINARY)
            contours1, hierarchy1 = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Todos os quadrados do board (contornos)
            for contour1 in contours1:
                (x1, y1, w1, h1) = cv2.boundingRect(contour1)

                # Validando se o quadrado se encaixa no esperado
                if isValid(h1, w1) :
                    crop_img1 = image[y+y1:y+y1+h1, x+x1:x+x1+w1]

                    # Processando a image para obter os contornos que existem dentro de cada quadrado do board
                    _, thresh2 = cv2.threshold(crop_img1, 115, 255, cv2.THRESH_BINARY_INV)
                    contours2, hierarchy2 = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                    isNumber = False
                    for contour2 in contours2:
                        (x2, y2, w2, h2) = cv2.boundingRect(contour2)
                        # print(x2,y2,w2,h2)

                        if w2 > 1 and h2 >= 1 : 
                            isNumber = True
                    
                    # Se existe algum sinal de cor dentro do quadrado do board, entende se que temos um numero ali
                    if isNumber :
                        cv2.rectangle(imgFinal, (x+x1+5, y+y1+5),(x+x1+w1-5, y+y1+h1-5), (0, 0, 255), 2)


   # Controle do slide show
    countingImg += 1
    countingImg = countingImg % 9
    if countingImg == 0 : 
        countingImg = 1

    cv2.imshow("img", imgFinal)
    key = cv2.waitKey(1000)
    if key == 113:
        break

