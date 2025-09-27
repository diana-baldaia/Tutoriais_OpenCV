import cv2 as cv
import sys

# Carregar a imagem
img = cv.imread(cv.samples.findFile("starry_night.jpg"))

# Verificar se a imagem foi carregada corretamente
if img is None:
    sys.exit("Could not read the image.")

# Exibir a imagem em uma janela
cv.imshow("Display window", img)

# Esperar por uma tecla ser pressionada, o parâmetro é o tempo de espera em milissegundos
# 0 significa esperar indefinidamente até que uma tecla seja pressionada
k = cv.waitKey(0)

# Se a tecla 's' for pressionada, salvar a imagem em disco
if k == ord("s"):
    cv.imwrite("starry_night.png", img)