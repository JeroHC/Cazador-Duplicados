"""
Crea la carpeta 'fotos_de_prueba' con "fotos" de ejemplo, como la galería
de un celular: fotos de la cámara, imágenes de WhatsApp, descargas y stickers.
Algunas están repetidas con OTRO nombre o en OTRA carpeta, como pasa de verdad.

No son fotos reales: son archivos con datos al azar del tamaño de una foto.
Se puede ejecutar las veces que quieras: siempre deja la carpeta como al inicio.
"""

from pathlib import Path
import os
import random
import shutil

CARPETA = Path("fotos_de_prueba")
random.seed(7)                                   # Siempre genera lo mismo

# Empieza desde cero cada vez
if CARPETA.exists():
    shutil.rmtree(CARPETA)
for sub in ["Camara", "WhatsApp Images", "Descargas", "Stickers"]:
    (CARPETA / sub).mkdir(parents=True)

# 20 fotos originales de la cámara, de entre 1 y 4 MB cada una
originales = []
for i in range(1, 21):
    contenido = os.urandom(random.randint(1, 4) * 1024 * 1024)
    ruta = CARPETA / "Camara" / f"IMG_202611{i:02d}_{random.randint(7, 22):02d}{random.randint(0, 59):02d}{random.randint(0, 59):02d}.jpg"
    ruta.write_bytes(contenido)
    originales.append(ruta)

# Copias con otros nombres: así las renombran WhatsApp y el navegador
copias = 0
contador_wa = 1
contador_desc = 0
for ruta in random.sample(originales, 9):
    for n in range(random.randint(1, 3)):
        if random.random() < 0.6:
            nuevo = CARPETA / "WhatsApp Images" / f"IMG-202611{random.randint(1, 18):02d}-WA{contador_wa:04d}.jpg"
            contador_wa += 1
        else:
            sufijo = f" ({contador_desc})" if contador_desc else ""
            nuevo = CARPETA / "Descargas" / f"descarga{sufijo}.jpg"
            contador_desc += 1
        shutil.copy(ruta, nuevo)
        copias += 1

# Stickers: archivos pequeños (menos de 1 MB) que también se repiten
for nombre in ["risa", "ok", "buenos_dias"]:
    contenido = os.urandom(random.randint(20, 300) * 1024)
    for n in range(random.randint(2, 4)):
        (CARPETA / "Stickers" / f"sticker_{nombre}_{n + 1}.webp").write_bytes(contenido)

total = sum(1 for a in CARPETA.rglob("*") if a.is_file())
print(f"Listo: '{CARPETA}' tiene {total} archivos, con copias escondidas.")
print("Ahora ejecuta:  python cazador_duplicados.py")
