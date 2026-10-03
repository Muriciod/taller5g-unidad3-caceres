"""Rosetas con Bresenham. Base: Unidad III, sección 2.3, página 12."""
from PIL import Image
import math
import colorsys
from pathlib import Path


def bresenham(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Bresenham generalizado del material, con aritmética entera."""
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    while True:
        if 0 <= x < ancho and 0 <= y < alto:
            pixels[x, y] = color
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy


def generar_puntos_circulo(cx, cy, radio, n):
    """Distribuye n puntos por ángulos iguales; redondea a píxeles."""
    puntos = []
    for i in range(n):
        angulo = 2 * math.pi * i / n
        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))
        puntos.append((x, y))
    return puntos


def dibujar_roseta(pixels, puntos, ancho, alto):
    """Conecta cada par una vez y colorea según orientación de la línea."""
    n = len(puntos)
    for i in range(n):
        for j in range(i + 1, n):
            x0, y0 = puntos[i]
            x1, y1 = puntos[j]
            # Orientación sin dirección: ángulos equivalentes módulo pi.
            angulo = math.atan2(y1-y0, x1-x0) % math.pi
            tono = angulo / math.pi
            rgb = colorsys.hsv_to_rgb(tono, 0.75, 1.0)
            color = tuple(round(c * 255) for c in rgb)
            bresenham(pixels, x0, y0, x1, y1, color, ancho, alto)


def main():
    salida = Path(__file__).resolve().parent
    for n in (12, 24, 36):
        # La circunferencia solo determina los puntos; no se dibuja.
        imagen = Image.new('RGB', (700, 700), 'black')
        puntos = generar_puntos_circulo(350, 350, 300, n)
        dibujar_roseta(imagen.load(), puntos, 700, 700)
        imagen.save(salida / f'roseta_{n}.png')
        if n == 24:
            imagen.save(salida / 'roseta.png')
        print(f'N={n}: {n*(n-1)//2} líneas')


if __name__ == '__main__':
    main()
