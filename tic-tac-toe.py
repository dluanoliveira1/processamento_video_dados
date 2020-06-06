import numpy as np
import cv2


def isValid(width, height):
    if width > 50 and width < 200:
        if height > width - 47 and height < width + 47:
            return True

def isCircle(img_crop) :
    image = img_crop
    output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.8, 100)

    if circles is not None:
        
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            return True
        
        return False

        # show the output image
        # cv2.imshow("output", np.hstack([image, output]))
        # cv2.waitKey(0)

def isSameLine(coordinates) :
    count = 0
    aux = 0 
    cInitial = 0
    for c in coordinates :
        if aux == 0 :
            cInitial = c[0]
            aux = 1

        if cInitial - 50 < c[0] and c[0] < cInitial + 50 :
            count += 1

        cInitial = c[0]

    if count == 3 :
        return True
    
    count = 0
    aux = 0 
    cInitial = 0
    for c in coordinates :
        if aux == 0 :
            cInitial = c[1]
            aux = 1

        if cInitial - 50 < c[1] and c[1] < cInitial + 50 :
            count += 1

        cInitial = c[1]

    if count == 3 :
        return True



def takeThird(elem):
    return elem[2]

def verifyBothWinning(coordinates) :

    os = []
    xs = []
    
    coordinates.sort(key=takeThird, reverse=False)
    for coord in coordinates :
        if(coord[2] == 0) :
             os.append(coord)
        elif(coord[2] == 1) :
             xs.append(coord)

    if isSameLine(os) and isSameLine(xs) :
        return True
    else:
        return False
        

def boardAnalysis(coordinates) :
    xs = 0
    os = 0
    for coordinate in coordinates :
        if coordinate[2] == 0 :
            os += 1
        else:
            xs += 1

    if (os >= 3 and xs >= 3) :
        if verifyBothWinning(coordinates) :
            cv2.putText(imgFinal, "Jogo Invalido", (30, 30), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (0, 200, 0), 1, cv2.LINE_AA)
        else :
            cv2.putText(imgFinal, "Jogo Valido", (30, 30), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (0, 200, 0), 1, cv2.LINE_AA)

    else :
        if abs(os - xs) > 1 :
            cv2.putText(imgFinal, "Jogo Invalido", (30, 30), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (0, 200, 0), 1, cv2.LINE_AA)
        else :
            cv2.putText(imgFinal, "Jogo Valido", (30, 30), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (0, 200, 0), 1, cv2.LINE_AA)
        


countingImg = 1
while True:

    # Imagem que será processada
    # imgUrl = "dados\\tic-tac-toe\\tic-tac-toe-20.jpg"

    imgUrl = "dados\\tic-tac-toe\\tic-tac-toe-" + str(countingImg) + ".jpg"

    # Imagem para escrever os resultados finais
    imgRef = cv2.imread(imgUrl)
    imgFinal = cv2.resize(imgRef, (700,700))

    # Imagem para utilizar durante processamento dos quadrados
    img = cv2.imread(imgUrl, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(img, (700,700))

    _, thresh = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    coordinates = []

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        print(x,y,w,h)

        if isValid(w, h) :
            cv2.rectangle(imgFinal, (x-20, y-20), (x+w+20, y+h+20), (0, 0, 255), 1)
            img_crop = imgFinal[y-20:y+h+20, x-20:x+w+20]
            

            if isCircle(img_crop) :
                coordinates.append([x,y,0])
                cv2.putText(imgFinal, "O", (x, y), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, (0, 200, 0), 1, cv2.LINE_AA)

            else :
                coordinates.append([x,y,1])
                cv2.putText(imgFinal, "X", (x, y), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, (0, 200, 0), 1, cv2.LINE_AA)


    xmiddle = 180
    ymiddle = 420
    img_crop1 = image[xmiddle:ymiddle, xmiddle:ymiddle]

    _, thresh = cv2.threshold(img_crop1, 180, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        print(x,y,w,h)

        if isValid(w, h) :
            cv2.rectangle(imgFinal, (x-20+xmiddle, y-20+xmiddle), (x+w+20+xmiddle, y+h+20+xmiddle), (0, 0, 255), 1)
            img_crop = imgFinal[y-20+xmiddle:y+h+20+xmiddle, x-20+xmiddle:x+w+20+xmiddle]
            

            if isCircle(img_crop) :
                coordinates.append([x+xmiddle,y+xmiddle,0])
                cv2.putText(imgFinal, "O", (x+xmiddle, y+xmiddle), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, (0, 200, 0), 1, cv2.LINE_AA)

            else :
                coordinates.append([x+xmiddle,y+xmiddle,1])
                cv2.putText(imgFinal, "X", (x+xmiddle, y+xmiddle), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, (0, 200, 0), 1, cv2.LINE_AA)
                
    # cv2.rectangle(imgFinal, (xmiddle, xmiddle - 20), (ymiddle, ymiddle), (0, 0, 255), 1)
    # if isCircle(img_crop1) :
    #     coordinates.append([xmiddle,ymiddle,0])
    #     cv2.putText(imgFinal, "O", (xmiddle, xmiddle), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, (0, 200, 0), 1, cv2.LINE_AA)
    # else :
    #     coordinates.append([xmiddle,ymiddle,1])
    #     cv2.putText(imgFinal, "X", (xmiddle, xmiddle), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, (0, 200, 0), 1, cv2.LINE_AA)
        
        
    

    boardAnalysis(coordinates)

    countingImg += 1
    countingImg = countingImg % 21
    if countingImg == 0 : 
        countingImg = 1

    

    cv2.imshow("img", imgFinal)
    # cv2.imshow("img2", img_crop1)
    key = cv2.waitKey(1000)
    if key == 113:
        break




# img = cv2.imread("dados\\tic-tac-toe.jpg")

# image = cv2.resize(img,(700,700))






            # cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            # cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)









# #create a 2d array to hold the gamestate
# gamestate = [["-","-","-"],["-","-","-"],["-","-","-"]]

# #kernel used for noise removal
# kernel =  np.ones((7,7),np.uint8)
# # Load a color image 
# img = cv2.imread("dados\\tic-tac-toe.jpg")
# # get the image width and height
# img_width = img.shape[0]
# img_height = img.shape[1]

# # turn into grayscale
# img_g =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # turn into thresholded binary
# ret,thresh1 = cv2.threshold(img_g,127,255,cv2.THRESH_BINARY)
# #remove noise from binary
# thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)

# #find and draw contours. RETR_EXTERNAL retrieves only the extreme outer contours
# contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img, contours, -1, (0,255,0), 15)

# tileCount = 0
# for cnt in contours:
#         # ignore small contours that are not tiles
#         if cv2.contourArea(cnt) > 200000: 
#                 tileCount = tileCount+1
#                 # use boundingrect to get coordinates of tile
#                 x,y,w,h = cv2.boundingRect(cnt)
#                 # create new image from binary, for further analysis. Trim off the edge that has a line
#                 tile = thresh1[x+40:x+w-80,y+40:y+h-80]
#                 # create new image from main image, so we can draw the contours easily
#                 imgTile = img[x+40:x+w-80,y+40:y+h-80]

#                 #determine the array indexes of the tile
#                 tileX = round((x/img_width)*3)
#                 tileY = round((y/img_height)*3)     

#                 # find contours in the tile image. RETR_TREE retrieves all of the contours and reconstructs a full hierarchy of nested contours.
#                 c, hierarchy = cv2.findContours(tile, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
#                 for ct in c:
#                         # to prevent the tile finding itself as contour
#                         if cv2.contourArea(ct) < 180000:
#                                 cv2.drawContours(imgTile, [ct], -1, (255,0,0), 15)
#                                 #calculate the solitity
#                                 area = cv2.contourArea(ct)
#                                 hull = cv2.convexHull(ct)
#                                 hull_area = cv2.contourArea(hull)
#                                 solidity = float(area)/hull_area

#                                 # fill the gamestate with the right sign
#                                 if(solidity > 0.5):
#                                         gamestate[tileX][tileY] = "O"
#                                 else: 
#                                         gamestate[tileX][tileY] = "X"
#                 # put a number in the tile
#                 cv2.putText(img, str(tileCount), (x+200,y+300), cv2.FONT_HERSHEY_SIMPLEX, 10, (0,0,255), 20)

# #print the gamestate
# print("Gamestate:")
# for line in gamestate:
#         linetxt = ""
#         for cel in line:
#                 linetxt = linetxt + "|" + cel
#         print(linetxt)

# # resize final image
# res = cv2.resize(img,None,fx=0.2, fy=0.2, interpolation = cv2.INTER_CUBIC)

# # display image and release resources when key is pressed
# cv2.imshow('image1',res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()