import cv2 as cv
import numpy as np

ordem = input("Pretende filmar (f) ou ver a gravação (v)? ")

if ordem == 'f':

    # Captura vídeo, o parâmetro 0 indica a webcam padrão
    cap = cv.VideoCapture(0)

    # Fourcc é um código de quatro caracteres que especifica o codec de vídeo
    fourcc = cv.VideoWriter_fourcc(*'XVID')

    # Cria o objeto VideoWriter para salvar o vídeo (nome, codec, fps, tamanho)
    out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))


    # Verifica se a câmera foi aberta corretamente
    if not cap.isOpened():
        print("Erro ao abrir a câmera")
        exit()

    while True:
        # Captura frame a frame
        ret, frame = cap.read()

        # Se o frame não for capturado corretamente, sai do loop
        if not ret:
            print("Erro ao capturar o frame")
            break

        # Converte o frame para escala de cinza
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Exibe o frame original e o frame em escala de cinza
        cv.imshow('Frame Original', frame)
        cv.imshow('Frame PB', gray)

        # Escreve o frame original no arquivo de vídeo
        out.write(frame)

        # Sai do loop se a tecla 'q' for pressionada
        if cv.waitKey(1) == ord('q'):
            break
    out.release()

elif ordem == 'v':

    # Captura o vídeo salvo
    cap = cv.VideoCapture('output.avi')

    # Verifica se o vídeo foi aberto corretamente
    if not cap.isOpened():
        print("Erro ao abrir o vídeo")
        exit()

    while True:
        # Captura frame a frame
        ret, frame = cap.read()

        # Se o frame não for capturado corretamente, sai do loop
        if not ret:
            print("Fim do vídeo ou erro ao capturar o frame")
            break

        # Exibe o frame
        cv.imshow('Frame Gravado', frame)

        # Sai do loop se a tecla 'q' for pressionada
        if cv.waitKey(25) == ord('q'):
            break

else:
    print("Comando inválido. Use 'f' para filmar ou 'v' para ver a gravação.")
    exit()


# Revela a captura
cap.release()
cv.destroyAllWindows()