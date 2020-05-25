import cv2
import numpy as np

# Funcão que define se os dados estão juntos (grudados)
def isValidaDouble(width, height):
    if width > height:
        if width > 70 and width < 110:
            return True
    else:
        if height > 70 and height < 110:
            return True

    return False

# Função que define se o tamanho é correspondente a um dado
def isValid(width, height):
    if width > 35 and width < 70:
        if height > width - 10 and height < width + 10:
            return True

    return False

# Função que identifica se o contorno da forma se manteve o mesmo após o frame
def equalContour(w, lW):
    if w >= lW - 3 and w <= lW + 3:
        return True

    return False

# Nesse função, é cortada a imagem de acordo com o tamanho e posição do dado, para então analisar o número do dado
def diceValue(x, y, w, h, img, imgFinal):

    # Recorta a imagem
    crop_img1 = img[y:y+h, x:x+w]
    crop_img = cv2.cvtColor(crop_img1, cv2.COLOR_BGR2GRAY)

    # Faz o trabalho pra identificar os Contours
    _, thresh1 = cv2.threshold(crop_img, 205, 255, cv2.THRESH_BINARY_INV)
    contours1, hierarchy1 = cv2.findContours(
        thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    countValue = 0

    for contour1 in contours1:
        (x2, y2, w2, h2) = cv2.boundingRect(contour1)

        if w2 > 5 and w2 < 10 and h2 > 5 and h2 < 10:
            # Desenha o contorno na Imagem final, a partir dos contours da imagem cortada (posição, tamanho)
            cv2.rectangle(imgFinal, (x2 + x, y2 + y),
                          (x2+w2+x, y2+h2+y), (255, 0, 0), 1)
            countValue += 1

    # Escreve o numero de pontos encontrado, na imagem final
    cv2.putText(imgFinal, str(countValue), ((x + np.int(w/2) - 12), (y + np.int(h/2) + 5)),
                cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, (0, 200, 0), 1, cv2.LINE_AA)


# Inicializando auxiliares
countFrame = 0
countWriteA = 0
countWriteB = 0
countWriteC = 0
countWriteD = 0
countContors = 0
countContorsA = 0
lastW = 0
lastW1 = 0
lastH = 0
lastH1 = 0
lastX = 0
lastX1 = 0
lastY = 0
lastY1 = 0
refA = 0
refB = 0

while True:
    cap = cv2.VideoCapture("dados/dados-video.mp4")  # Acessando vídeo dos dados
    cap.set(1, countFrame)  # Setando os frames
    ret, frame = cap.read()  # Acessando um frame para analise
    ret, frameFinal = cap.read()

    # Transformando a imagem em escala de cinza
    g_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Definindo área dos dados - threshDados
    _, thresh = cv2.threshold(g_image, 245, 255, cv2.THRESH_BINARY)

    # Pegando os contornos dos dados das áreas dos dados
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Acessando todas as formas encontradas na imagem
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        print(x, y, w, h)
        if isValid(w, h):
            countContors += 1
            countWriteC = 0
            countWriteD = 0

            # A lógica dentro desse if é para identificar se os frames estão se repetindo, uma vez que se repetem x vezes, podemos mostrar o resultado
            if countContors == 1:
                if equalContour(w, lastW) and equalContour(x, lastX) and equalContour(h, lastH) and equalContour(y, lastY):
                    countWriteA += 1
                else:
                    countWriteA = 0

                lastW = w
                lastH = h
                lastX = x
                lastY = y
            if countContors == 2:
                if equalContour(w, lastW1) and equalContour(x, lastX1) and equalContour(h, lastH1) and equalContour(y, lastY1):
                    countWriteB += 1
                else:
                    countWriteB = 0

                lastW1 = w
                lastH1 = h
                lastX1 = x
                lastY1 = y

        elif isValidaDouble(w, h):
            countContorsA += 1
            countWriteA = 0
            countWriteB = 0
            if h > w:
                refA = (int)(y + (h/2))
                if equalContour(int(h/2), lastH) and equalContour(x, lastX) and equalContour(w, lastW) and equalContour(y, lastY):
                    countWriteC += 1
                else:
                    countWriteC = 0

                lastW = w
                lastH = int(h/2)
                lastX = x
                lastY = y
                lastW1 = w
                lastH1 = int(h/2)
                lastX1 = x
                lastY1 = refA
            else:
                refA = (int)(x + (w/2))
                if equalContour((int)(w/2), lastW) and equalContour(x, lastX) and equalContour(h, lastH) and equalContour(y, lastY):
                    countWriteD += 1
                else:
                    countWriteD = 0

                lastW = (int)(w/2)
                lastH = h
                lastX = x
                lastY = y
                lastW1 = (int)(w/2)
                lastH1 = h
                lastX1 = refA
                lastY1 = y

    # Limpando variaveis
    if countContors == 0:
        countWriteA = 0
        countWriteB = 0
    # Limpando variaveis
    if countContorsA == 0:
        countWriteC = 0
        countWriteD = 0
    
    # Logica para um dos dados (após 15 frames, chamaremos a função para identificar do dado (diceValue))
    if countWriteA > 15:
        diceValue(lastX, lastY, lastW, lastH, frame, frameFinal)
        cv2.rectangle(frameFinal, (lastX, lastY),
                      (lastX+lastW, lastY+lastH), (0, 0, 255), 1)

    # Logica para o dado remanescente (após 15 frames passando pela validação que se manteve +-3 comparando com o anterior, 
    # chamaremos a função para identificar do dado (diceValue))
    if countWriteB > 15:
        diceValue(lastX1, lastY1, lastW1, lastH1, frame, frameFinal)
        cv2.rectangle(frameFinal, (lastX1, lastY1),
                      (lastX1+lastW1, lastY1+lastH1), (0, 0, 255), 1)

    # Logica para os dados juntos (chama diceVlaue após 18 frames que passam pela doubleValid, 
    # que identifica se o frame manteve-se o mesmo, com uma carencia +-3)
    if countWriteC > 18:
        diceValue(lastX, lastY, lastW, lastH, frame, frameFinal)
        diceValue(lastX1, lastY1, lastW1, lastH1, frame, frameFinal)
        cv2.rectangle(frameFinal, (lastX, lastY),
                      (lastX+lastW, lastY+lastH), (0, 0, 255), 1)
        cv2.rectangle(frameFinal, (lastX1, lastY1),
                      (lastX1+lastW1, lastY1+lastH1), (0, 0, 255), 1)

    # Mesma coisa que o anterior, porem para os dados na outra posição (um vertical e outro horizontal)
    if countWriteD > 18:
        diceValue(lastX, lastY, lastW, lastH, frame, frameFinal)
        diceValue(lastX1, lastY1, lastW1, lastH1, frame, frameFinal)
        cv2.rectangle(frameFinal, (lastX, lastY),
                      (lastX+lastW, lastY+lastH), (0, 0, 255), 1)
        cv2.rectangle(frameFinal, (lastX1, lastY1),
                      (lastX1+lastW1, lastY1+lastH1), (0, 0, 255), 1)

    # Counting ++ e limpando variaveis
    countFrame += 1
    countContors = 0
    countContorsA = 0

    print('\n')
    print(countFrame)

    cv2.imshow("FrameByFrame", frameFinal)
    # cv2.imshow("Mask", thresh)

    key = cv2.waitKey(1)
    if key == 113:
        break

    if countFrame == 4090:
        break

    # if key == 97:
    #     countFrame -= 1
    # if key == 100:
    #     countFrame += 1

cap.release()
cv2.destroyAllWindows()
