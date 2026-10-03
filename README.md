# Conversión por rastreo — Unidad III

Alumno: Mauricio Cáceres  
Materia: Taller de Programación de 5.ª Generación I  
Docente: Prof. Mgtr. Alberto F. Giménez Méndez

## Ejecución
Requiere Python 3 y Pillow. Desde esta carpeta:

```bash
python -m pip install -r requirements.txt
python ejercicio1_casa.py
python ejercicio2_roseta.py
```

Los archivos se guardan junto a los scripts, independientemente del directorio desde el cual se ejecuten.

- `ejercicio1_casa.py`: casa de 600 × 500, con DDA y árboles como extensión.
- `ejercicio2_roseta.py`: rosetas de 700 × 700 con Bresenham y gradiente angular.
- `casa.png`, `roseta_12.png`, `roseta_24.png`, `roseta_36.png`: resultados requeridos.
- `roseta.png`: copia de la variante N=24 requerida como salida base.
- `Entrega_Unidad_III.docx`: informe con las cuatro imágenes y descripción.

N=12: 66 líneas; N=24: 276 líneas; N=36: 630 líneas.
Los algoritmos se reutilizan del material de lectura, secciones 2.2 y 2.3, páginas 9–12. DDA conserva incluso el retorno sin dibujar cuando ambos extremos coinciden; las figuras no utilizan segmentos degenerados.
