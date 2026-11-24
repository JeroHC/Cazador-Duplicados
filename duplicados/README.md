# Cazador de Duplicados

Revisa una carpeta y sus subcarpetas y encuentra los archivos repetidos, **aunque tengan nombres distintos**. Al final dice cuántos archivos sobran y cuánto espacio desperdician.

> Este README es el punto de partida. Mejorarlo es uno de los issues del equipo.

## Cómo usarlo

Solo necesitas Python. No hay que instalar nada, ni crear un entorno virtual.

```
python crear_fotos.py            # crea una galería de prueba con fotos repetidas
python cazador_duplicados.py     # encuentra las repetidas
```

Si `python` no funciona en tu computador, usa `py`.

`crear_fotos.py` se puede ejecutar las veces que quieras: siempre deja la galería como al inicio. Así pruebas sin riesgo, sin tocar tus fotos reales.

El script **no borra ni mueve nada**: solo muestra lo que encontró.

## ¿Cómo sabe que dos archivos son iguales?

No compara los nombres: `IMG-20261103-WA0003.jpg` y `descarga (2).jpg` pueden ser la misma foto. Lo que hace es calcular una **huella digital** (un *hash*) del contenido de cada archivo. Si dos archivos tienen la misma huella, son idénticos.

La huella **no viene guardada en la foto**: el script la calcula leyendo el contenido del archivo, cada vez que se ejecuta. Si cambia un solo byte, la huella cambia por completo.

Es la misma idea que usa Git para identificar cada commit, y la que usan Google Drive y Dropbox para no guardar dos veces el mismo archivo.

## Lo que NO detecta

Solo encuentra copias **idénticas**. Cuando envías una foto por WhatsApp, la app la **comprime** para que pese menos: se ve igual, pero su contenido ya es otro, y su huella también. Por eso la foto de tu cámara y la que te llegó por WhatsApp **no salen como repetidas**.

Sí detecta la misma foto descargada dos veces, reenviada tal cual o copiada a otra carpeta.

Encontrar fotos *parecidas* (no idénticas) es otro problema, que se resuelve con técnicas como el *hash perceptual* y librerías externas.

## Lo que vas a aprender con este script

| Concepto | Dónde está en el código | Qué hace |
|---|---|---|
| **Variable** | `CARPETA = Path("fotos_de_prueba")` | Guarda un dato para usarlo después |
| **Diccionario** | `grupos = {}` | Relaciona cada huella con la lista de archivos que la tienen |
| **Lista** | `[archivo1, archivo2]` | Guarda varios valores en orden |
| **Función** | `def huella(archivo):` | Un bloque de código con nombre, que se puede usar muchas veces |
| **Ciclo `for`** | `for archivo in carpeta.rglob("*"):` | Repite lo mismo con cada archivo, incluidas las subcarpetas |
| **Condicional `if`** | `if archivo.is_file():` | Decide qué hacer según una condición |
| **Contador** | `revisados += 1` | Suma uno cada vez que revisa un archivo |
| **Módulos** | `import hashlib`, `import time` | Herramientas que ya trae Python: calcular huellas y medir el tiempo |
| **f-string** | `f"Revisé {revisados} archivos"` | Arma un texto con valores adentro |

## Cómo está organizado el código

1. **Configuración** (arriba): la carpeta que se va a revisar.
2. **`huella()`**: calcula la huella digital de un archivo.
3. **`buscar_duplicados()`**: recorre la carpeta, agrupa los archivos por huella y se queda con los grupos repetidos.
4. **`tamano_legible()`**: convierte bytes a KB, MB o GB.
5. **`mostrar_resultados()`**: muestra cada grupo y calcula cuántos archivos sobran y cuánto ocupan.
6. **`if __name__ == "__main__":`**: lo que se ejecuta cuando corres `python cazador_duplicados.py`.
