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

## Completar antes de entregar
1. Añadir la matrícula al Word.
2. Crear el repositorio `taller5g-unidad3-caceres` en GitHub o GitLab y subir los archivos de esta carpeta.
3. Copiar su URL real al Word. Si es privado, dar acceso al docente según la consigna.
4. Verificar el acceso, guardar el Word actualizado y volver a comprimir esta carpeta.
5. Subir el ZIP a Canvas.

No se incluye una URL ficticia ni se afirma que el repositorio ya fue publicado.
