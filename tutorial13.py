import cv2 as cv
import numpy as np

# Criar uma imagem preta, 512x512 pixels, 3 canais (BGR), 8 bits por canal, preenchida com zeros (preto)
img = np.zeros((512, 512, 3), np.uint8)

# Desenhar uma linha azul (255, 0, 0) grossa (5 pixels) do canto superior esquerdo (0, 0) ao canto inferior direito (511, 511)
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Desenhar um retângulo verde (0, 255, 0) com borda grossa (3 pixels) do ponto (384, 0) ao ponto (510, 128)
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# Desenhar um círculo vermelho (0, 0, 255) preenchido (espessura -1) com centro em (447, 63) e raio 63
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

# Desenhar uma elipse amarela (0, 255, 255) com borda grossa (2 pixels), centrada em (256, 256), 
# com eixos maiores 100 e menores 50, rotacionada em 0 graus, de 0 a 360 graus
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 360, (0, 255, 255), 2)

# Desenhar um polígono branco (255, 255, 255) com borda grossa (3 pixels) usando os pontos fornecidos
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# Reshape os pontos para o formato necessário, (-1, 1, 2), onde -1 infere o número de pontos, 1 é o número de canais e 2 são as coordenadas x, y
pts = pts.reshape((-1, 1, 2))
# O argumento True indica que o polígono deve ser fechado
cv.polylines(img, [pts], True, (255, 255, 255), 3)

# Adicionar texto "OpenCV" em azul (255, 0, 0) na posição (10, 500) com a fonte FONT_HERSHEY_SIMPLEX,
# escala 4, espessura 2 e tipo de linha cv.LINE_AA (antialiased)
cv.putText(img, 'OpenCV', (10, 500), cv.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2, cv.LINE_AA)

# Exibir a imagem em uma janela chamada 'Imagem'
cv.imshow('Imagem', img)
# Esperar até que uma tecla seja pressionada
cv.waitKey(0)
# Fechar todas as janelas abertas
cv.destroyAllWindows()
# Salvar a imagem em um arquivo chamado 'drawing.png'
cv.imwrite('drawing.png', img)