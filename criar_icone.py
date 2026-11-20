"""Gera o ícone do executável a partir de Pasta_Vermelha.png:
1. remove o fundo quadriculado (branco/cinza) em volta da pasta, deixando-o transparente;
2. escreve "PDF" na pasta;
3. salva Pasta_Vermelha_PDF.png e icone.ico.
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from scipy import ndimage

img = Image.open("Pasta_Vermelha.png").convert("RGBA")
#icone.ico
# ---------- 1. Remover o fundo ----------
rgb = np.asarray(img)[:, :, :3].astype(int)
brilho = rgb.max(axis=2)
saturacao = rgb.max(axis=2) - rgb.min(axis=2)

# Pixels "tipo fundo": cinza/branco claro (o xadrez)
parece_fundo = (saturacao < 30) & (brilho > 150)

# Só é fundo de verdade o que está ligado à borda da imagem
# (assim a folha branca e os brilhos dentro da pasta não são apagados)
rotulos, _ = ndimage.label(parece_fundo)
na_borda = np.unique(np.concatenate([rotulos[0], rotulos[-1], rotulos[:, 0], rotulos[:, -1]]))
fundo = np.isin(rotulos, na_borda[na_borda > 0])

# Fica só a pasta: maior pedaço que sobrou (descarta riscos soltos do fundo)
pasta = ~fundo
rotulos, n = ndimage.label(pasta)
tamanhos = ndimage.sum(pasta, rotulos, range(1, n + 1))
pasta = rotulos == (np.argmax(tamanhos) + 1)
pasta = ndimage.binary_fill_holes(pasta)
pasta = ndimage.binary_erosion(pasta, iterations=3)  # tira a franja clara do contorno

# Borda suave (anti-serrilhado)
alfa = Image.fromarray((pasta * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
img.putalpha(alfa)

# Recorta o espaço vazio em volta
img = img.crop(img.getbbox())

# ---------- 2. Escrever "PDF" ----------
draw = ImageDraw.Draw(img)
fonte = ImageFont.truetype("C:/Windows/Fonts/ariblk.ttf", 165)  # Arial Black
texto = "PDF"

# Centro da parte vermelha livre da pasta (à esquerda da folha),
# em coordenadas da imagem original, ajustado pelo recorte
topo, esq = np.argwhere(pasta).min(axis=0)
centro_x, centro_y = 385 - esq, 620 - topo

x0, y0, x1, y1 = draw.textbbox((0, 0), texto, font=fonte)
x = centro_x - (x1 - x0) / 2 - x0
y = centro_y - (y1 - y0) / 2 - y0
draw.text((x + 8, y + 8), texto, font=fonte, fill=(90, 0, 0, 160))   # sombra
draw.text((x, y), texto, font=fonte, fill="white", stroke_width=6, stroke_fill=(120, 0, 0))

img.save("Pasta_Vermelha_PDF.png")

# ---------- 3. Ícone do Windows (precisa ser quadrado) ----------
lado = max(img.size)
quadrado = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
quadrado.paste(img, ((lado - img.width) // 2, (lado - img.height) // 2), img)
quadrado.save("icone.ico", sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
print("icone.ico criado")
