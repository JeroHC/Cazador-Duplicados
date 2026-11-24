# Issues del Cazador de Duplicados

El líder del equipo crea estos issues en GitHub (**Issues → New issue**), copiando el título y la descripción, y le asigna cada uno a un integrante (**Assignees**). Las etiquetas (**Labels**) ya vienen en GitHub.

Van del más fácil al más difícil. Equipo de 2: issues 1 a 4 · equipo de 3: 1 a 6 · equipo de 4: 1 a 6, más uno que propongan ustedes.

---

## 1. `docs: mejorar el README`
**Label:** `documentation`

Completar el README para que alguien que no conoce el proyecto lo entienda: qué problema resuelve, cómo se usa, un ejemplo de lo que muestra en pantalla y quiénes lo hicieron.

**Listo cuando:**
- [ ] El README explica qué hace y cómo se usa
- [ ] Tiene un ejemplo de la salida
- [ ] Tiene los nombres del equipo

---

## 2. `feat: ignorar archivos pequeños`
**Label:** `good first issue`

Los stickers y los archivos pequeños no ocupan casi espacio, y llenan el reporte. Agregar en la configuración un tamaño mínimo (por ejemplo, 1 MB) y no revisar los archivos más pequeños.

**Listo cuando:**
- [ ] Hay una variable de configuración con el tamaño mínimo
- [ ] Los stickers ya no aparecen en el reporte
- [ ] Lo probé con `crear_fotos.py`
- [ ] Actualicé el README con este cambio

---

## 3. `feat: mostrar primero los grupos que más espacio ocupan`
**Label:** `enhancement`

Hoy los grupos salen en cualquier orden. Ordenarlos para que primero salgan los que más espacio desperdician, y mostrar ese espacio en cada grupo. Por ejemplo:
```
Grupo 1: 4 copias idénticas (sobran 12.0 MB)
```

**Listo cuando:**
- [ ] Los grupos salen de mayor a menor espacio desperdiciado
- [ ] Cada grupo muestra cuánto espacio sobra
- [ ] Actualicé el README con este cambio

---

## 4. `feat: guardar el reporte en reporte.csv`
**Label:** `enhancement`

Además de mostrar el resultado en pantalla, guardar los archivos repetidos en `reporte.csv`, con estas columnas:
```
grupo,archivo,carpeta,tamano_mb
```
Cada vez que se ejecute, el reporte se reemplaza por uno nuevo.

**Pista:** usen el módulo `csv`, que ya viene con Python. Para que Excel muestre bien las tildes y las eñes, abran el archivo con `encoding="utf-8-sig"`. Si al abrirlo en Excel todo queda en una sola columna, separen con punto y coma: `csv.writer(archivo, delimiter=";")`.

**Listo cuando:**
- [ ] Se crea `reporte.csv` con las cuatro columnas
- [ ] Se abre bien en Excel: cada dato en su columna, con tildes y eñes
- [ ] Actualicé el README con este cambio

---

## 5. `feat: mover los repetidos a una carpeta "repetidos"`
**Label:** `enhancement`

Encontrar los repetidos es la mitad del trabajo. De cada grupo, dejar **un** archivo donde está y mover las demás copias a una carpeta `repetidos`. No se borra nada: si alguien se equivoca, puede recuperar sus fotos. Al final, mostrar cuánto espacio se liberó.

Ojo: dos copias pueden llamarse igual en carpetas distintas. Si ya existe un archivo con ese nombre en `repetidos`, hay que renombrar el nuevo para no perderlo.

**Listo cuando:**
- [ ] En cada grupo queda un archivo en su lugar
- [ ] Las copias quedan en `repetidos`, sin perder ninguna
- [ ] Al ejecutar otra vez el cazador, ya no encuentra repetidos fuera de `repetidos`
- [ ] Muestra cuántos MB se liberaron
- [ ] Actualicé el README con este cambio

---

## 6. `feat: usarlo con mis Imágenes de verdad`
**Label:** `enhancement`

Cambiar la carpeta por la carpeta de Imágenes real del computador y, **antes de revisar, preguntar**:
```
Voy a revisar C:\Users\...\Pictures. ¿Continuar? (s/n)
```
Si la respuesta no es `s`, no se hace nada. Con la carpeta real **solo se muestran los resultados: no se mueve nada**.

**Listo cuando:**
- [ ] Encuentra la carpeta de Imágenes del usuario (pista: `Path.home() / "Pictures"`)
- [ ] Pregunta antes de revisar y respeta la respuesta
- [ ] Con la carpeta real no mueve ningún archivo
- [ ] Lo probé primero con la carpeta de prueba
- [ ] Actualicé el README con este cambio

---

## 7. (Equipos de 4) Su propia mejora
**Label:** `enhancement`

Propongan una mejora o una forma de aplicar el cazador a algo real: su proyecto formativo, su trabajo, su celular, una memoria USB. Escriban el issue ustedes mismos, con su lista de **Listo cuando**, que incluya actualizar el README.
