"""
CAZADOR DE ARCHIVOS DUPLICADOS
==============================
Revisa una carpeta (y sus subcarpetas) y encuentra los archivos repetidos,
aunque tengan nombres distintos. Al final dice cuánto espacio desperdician.

¿Cómo sabe que dos archivos son iguales? Calcula una "huella digital"
(un hash) de su CONTENIDO. Si dos archivos tienen la misma huella,
son idénticos, sin importar cómo se llamen ni en qué carpeta estén.

Cómo usarlo:
    1. Crea la carpeta de prueba:   python crear_fotos.py
    2. Busca los duplicados:        python cazador_duplicados.py

(Si "python" no funciona en tu computador, usa "py").

No hay que instalar nada: solo usa módulos que ya vienen con Python.
No borra ni mueve nada: solo muestra lo que encontró.
"""

from pathlib import Path   # Para trabajar con carpetas y archivos
import hashlib             # Para calcular la huella digital (hash) de cada archivo
import time                # Para medir cuánto se demora

# ------------------------------------------------------------------
# CONFIGURACIÓN: la carpeta que se va a revisar
# ------------------------------------------------------------------
CARPETA = Path("fotos_de_prueba")


def huella(archivo):
    """Calcula la huella digital (SHA-256) del contenido de un archivo."""
    h = hashlib.sha256()
    with open(archivo, "rb") as f:                 # "rb": leer en binario
        # Lee el archivo por partes de 64 KB: así funciona con archivos grandes
        for bloque in iter(lambda: f.read(65536), b""):
            h.update(bloque)
    return h.hexdigest()


def buscar_duplicados(carpeta):
    """Agrupa los archivos por huella.

    Devuelve dos cosas: la lista de grupos con repetidos
    y cuántos archivos revisó en total.
    """
    grupos = {}                                    # huella -> lista de archivos con esa huella
    revisados = 0
    for archivo in carpeta.rglob("*"):             # rglob: incluye las subcarpetas
        if archivo.is_file():
            grupos.setdefault(huella(archivo), []).append(archivo)
            revisados += 1
    repetidos = [lista for lista in grupos.values() if len(lista) > 1]
    return repetidos, revisados


def tamano_legible(bytes_):
    """Convierte bytes a KB, MB o GB para que se lea fácil."""
    for unidad in ["B", "KB", "MB", "GB"]:
        if bytes_ < 1024:
            return f"{bytes_:.1f} {unidad}"
        bytes_ /= 1024
    return f"{bytes_:.1f} TB"


def mostrar_resultados(duplicados):
    """Muestra cada grupo de copias y devuelve cuántas sobran y cuánto ocupan."""
    sobrantes = 0
    espacio = 0
    for numero, grupo in enumerate(duplicados, start=1):
        print(f"Grupo {numero}: {len(grupo)} copias idénticas")
        for archivo in grupo:
            print(f"   - {archivo}")
        # Se conserva 1 copia; las demás son espacio desperdiciado
        sobrantes += len(grupo) - 1
        espacio += grupo[0].stat().st_size * (len(grupo) - 1)
    return sobrantes, espacio


if __name__ == "__main__":
    if not CARPETA.exists():
        print(f"No encontré la carpeta '{CARPETA}'. ¿Ejecutaste crear_fotos.py?")
        raise SystemExit

    print(f"Buscando duplicados en '{CARPETA}'...\n")
    inicio = time.time()
    duplicados, revisados = buscar_duplicados(CARPETA)
    sobrantes, espacio = mostrar_resultados(duplicados)
    segundos = time.time() - inicio

    print("\n" + "=" * 55)
    print(f"Revisé {revisados} archivos en {segundos:.2f} segundos.")
    print(f"Encontré {sobrantes} archivos repetidos que ocupan {tamano_legible(espacio)}.")
    print("=" * 55)
