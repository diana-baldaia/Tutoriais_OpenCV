import cv2 as cv
import numpy as np

# Ver a lista de eventos possíveis com o rato
"""
events = [i for i in dir(cv) if 'EVENT' in i]
print( events )
"""

drawing = False # True se o rato estiver pressionado
mode = True    # Se True, desenha retângulos. Precione 'm' para alternar para círculos
ix, iy = -1, -1 # Coordenadas iniciais

# Função callback do rato
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode # Variáveis globais

    if event == cv.EVENT_LBUTTONDOWN: # Botão esquerdo do rato pressionado
        drawing = True # Começar a desenhar
        ix, iy = x, y # Guardar as coordenadas iniciais

    elif event == cv.EVENT_MOUSEMOVE: # Movimento do rato
        if drawing == True: # Desenhar apenas se o botão do rato estiver pressionado
            if mode == True: # Desenhar retângulo ou círculo
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 0) 
            else:
                cv.circle(img, (x, y), 5, (0, 0, 255), -1)

    elif event == cv.EVENT_LBUTTONUP: # Botão esquerdo do rato solto
        drawing = False # Parar de desenhar
        if mode == True: # Desenhar retângulo ou círculo
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 0)
        else:
            cv.circle(img, (x, y), 5, (0, 0, 255), -1)

# Criar uma imagem preta
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image') # Criar uma janela
cv.setMouseCallback('image', draw_circle) # Associar a função callback do rato à janela

while(1):
    cv.imshow('image', img) # Mostrar a imagem
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'): # Pressionar 'm' para alternar entre retângulo e círculo
        mode = not mode
    elif k == 27: # Pressionar 'ESC' para sair
        break

cv.destroyAllWindows()   # Fechar todas as janelas