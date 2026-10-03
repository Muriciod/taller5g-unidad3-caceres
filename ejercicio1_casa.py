"""Casa con DDA. Base: Unidad III, sección 2.2, páginas 9 y 10."""
from PIL import Image
import math
from pathlib import Path


def dda(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Traza una línea usando la implementación DDA del material."""
    dx = x1 - x0
    dy = y1 - y0
    pasos = max(abs(dx), abs(dy))
    if pasos == 0:
        return
    x_inc = dx / pasos
    y_inc = dy / pasos
    x, y = x0, y0
    for _ in range(int(pasos) + 1):
        px, py = round(x), round(y)
        if 0 <= px < ancho and 0 <= py < alto:
            pixels[px, py] = color
        x += x_inc
        y += y_inc


def dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Conecta las cuatro esquinas mediante cuatro segmentos DDA."""
    for a, b in [((x0,y0),(x1,y0)), ((x1,y0),(x1,y1)),
                 ((x1,y1),(x0,y1)), ((x0,y1),(x0,y0))]:
        dda(pixels, *a, *b, color, ancho, alto)


def dibujar_triangulo(pixels, p1, p2, p3, color, ancho, alto):
    """Cierra los tres lados del techo o de la copa de un árbol."""
    for a, b in [(p1,p2), (p2,p3), (p3,p1)]:
        dda(pixels, *a, *b, color, ancho, alto)


def dibujar_puerta(pixels, x, y, ancho, alto):
    """Puerta rectangular marrón y picaporte construido con segmentos."""
    dibujar_rectangulo(pixels, x, y, x+60, y+110, (125,65,30), ancho, alto)
    dibujar_rectangulo(pixels, x+46, y+56, x+50, y+60, (125,65,30), ancho, alto)


def dibujar_ventana(pixels, x, y, color, ancho, alto):
    """Ventana cuadrada de 55 píxeles de lado con dos divisiones."""
    dibujar_rectangulo(pixels, x, y, x+55, y+55, color, ancho, alto)
    dda(pixels, x+27, y, x+27, y+55, color, ancho, alto)
    dda(pixels, x, y+27, x+55, y+27, color, ancho, alto)


def dibujar_sol(pixels, cx, cy, radio, n_rayos, color, ancho, alto):
    """Calcula los extremos polares de rayos que parten del centro."""
    for i in range(n_rayos):
        angulo = 2 * math.pi * i / n_rayos
        x = cx + round(radio * math.cos(angulo))
        y = cy + round(radio * math.sin(angulo))
        dda(pixels, cx, cy, x, y, color, ancho, alto)


def dibujar_piso(pixels, ancho, alto):
    """Traza el piso de borde a borde del lienzo."""
    dda(pixels, 0, 430, ancho-1, 430, (55,110,45), ancho, alto)


def dibujar_arbol(pixels, cx, ancho, alto):
    """Extensión voluntaria: tronco rectangular y copa triangular."""
    dibujar_rectangulo(pixels, cx-10, 365, cx+10, 429, (115,85,55), ancho, alto)
    dibujar_triangulo(pixels, (cx,265), (cx-48,365), (cx+48,365),
                     (25,135,70), ancho, alto)


def main():
    # Pillow solo crea y guarda el frame buffer; todas las líneas usan DDA.
    ancho, alto = 600, 500
    imagen = Image.new('RGB', (ancho, alto), (225,242,255))
    pixels = imagen.load()
    dibujar_rectangulo(pixels, 160, 230, 440, 429, (35,85,165), ancho, alto)
    dibujar_triangulo(pixels, (140,230), (300,115), (460,230),
                     (205,55,55), ancho, alto)
    dibujar_puerta(pixels, 270, 319, ancho, alto)
    dibujar_ventana(pixels, 190, 265, (0,135,160), ancho, alto)
    dibujar_ventana(pixels, 355, 265, (145,65,180), ancho, alto)
    dibujar_sol(pixels, 510, 85, 44, 16, (235,160,0), ancho, alto)
    dibujar_arbol(pixels, 75, ancho, alto)
    dibujar_arbol(pixels, 525, ancho, alto)
    dibujar_piso(pixels, ancho, alto)
    imagen.save(Path(__file__).resolve().parent / 'casa.png')


if __name__ == '__main__':
    main()
