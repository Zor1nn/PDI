from re import A
import numpy as np
import cv2 as cv
import os


PRETO = 0
BRANCO = 255
DIRNAME = os.path.dirname(__file__) # pega o  diretório do programa

def main():

    nome = input("Insira o nome com o tipo da imagem que deseja trabalhar: ")
    t = int(input("Insira o limiar desejado: "))
    acima = input("Deseja alterar os tons de cinza acima do limiar <S> ou <N>?: ")
    brilho = int(input("Insira o valor do brilho: "))

    img = cv.imread(DIRNAME + "\\" + nome)
    imgAux = img.astype(np.int32)


    if acima == "S":
        imgAux[imgAux >= t] += brilho
        imgAux[imgAux > BRANCO] = 255
        imgAux[imgAux < PRETO] = 0

        imgAux = imgAux.astype(np.uint8)

        cv.imshow("image in", img)
        cv.imshow("image out", imgAux)
        print(img)
        print(imgAux)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif acima == "N":
        imgAux[imgAux < t] += brilho
        imgAux[imgAux > BRANCO] = 255
        imgAux[imgAux < PRETO] = 0

        imgAux = imgAux.astype(np.uint8)
        
        cv.imshow("image in", img)
        cv.imshow("image out", imgAux)
        print(img)
        print(imgAux)
        cv.waitKey(0)
        cv.destroyAllWindows()

    else:
        print("Erro!")



if __name__ == '__main__':
	main()