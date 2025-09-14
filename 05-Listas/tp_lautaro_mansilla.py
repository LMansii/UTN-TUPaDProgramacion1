#1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

notas = [7, 8, 5, 9, 10, 6, 4, 8, 7, 9]

print("Notas de los estudiantes:", notas)

promedio = sum(notas) / len(notas)
print("Promedio de las notas:", promedio)

nota_maxima = max(notas)
print("Nota más alta:", nota_maxima)

nota_minima = min(notas)
print("Nota más baja:", nota_minima)

# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)

productos_ordenados = sorted(productos)
print("\nLista de productos ordenada alfabéticamente:")
print(productos_ordenados)

eliminar = input("\n¿Qué producto desea eliminar?: ")

if eliminar in productos_ordenados:
    productos_ordenados.remove(eliminar)
    print("\nLista actualizada de productos:")
    print(productos_ordenados)
else:
    print(f"\nEl producto '{eliminar}' no está en la lista.")

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

numeros = [random.randint(1, 100) for _ in range(15)]
print("Lista de números generados:", numeros)

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("\nNúmeros pares:", pares)
print("Cantidad de pares:", len(pares))

print("\nNúmeros impares:", impares)
print("Cantidad de impares:", len(impares))

# 4) Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
print("Lista original:", datos)

sin_repetidos = list(set(datos))

print("Lista sin elementos repetidos:", sin_repetidos)

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = []
for i in range(8):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ").strip()
    estudiantes.append(nombre)

print("\nEstudiantes presentes:")
print(estudiantes)

accion = input("\n¿Querés AGREGAR o ELIMINAR un estudiante? (a/e, enter para no cambiar): ").strip().lower()

if accion == "a":
    nuevo = input("Nombre a agregar: ").strip()
    if nuevo in estudiantes:
        print(f"'{nuevo}' ya estaba en la lista.")
    else:
        estudiantes.append(nuevo)
        print(f"Agregado '{nuevo}'.")
elif accion == "e":
    quitar = input("Nombre a eliminar: ").strip()
    idx = next((i for i, n in enumerate(estudiantes) if n.lower() == quitar.lower()), -1)
    if idx != -1:
        eliminado = estudiantes.pop(idx)
        print(f"Eliminado '{eliminado}'.")
    else:
        print(f"No encontré '{quitar}' en la lista.")
else:
    print("Sin cambios.")

print("\nLista final actualizada:")
print(estudiantes)


# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

nums = [10, 20, 30, 40, 50, 60, 70]
print("\nLista original:", nums)

rotada = [nums[-1]] + nums[:-1]
print("Lista rotada (derecha, 1 posición):", rotada)

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
temperaturas = []

print("\nIngresá las temperaturas (mín y máx) de la semana:")
for i, dia in enumerate(dias, start=1):
    tmin = float(input(f"{dia} - Mínima: "))
    tmax = float(input(f"{dia} - Máxima: "))
    if tmax < tmin:
        print("⚠️ La máxima no puede ser menor que la mínima. Intercambio los valores.")
        tmin, tmax = tmax, tmin
    temperaturas.append([tmin, tmax])

prom_min = sum(fila[0] for fila in temperaturas) / 7
prom_max = sum(fila[1] for fila in temperaturas) / 7

amplitudes = [fila[1] - fila[0] for fila in temperaturas]
idx_max_amp = amplitudes.index(max(amplitudes))

print("\nMatriz (mín, máx) por día:")
for d, (mn, mx) in zip(dias, temperaturas):
    print(f"{d}: ({mn}, {mx})")

print(f"\nPromedio de mínimas: {prom_min:.2f}")
print(f"Promedio de máximas: {prom_max:.2f}")
print(f"Mayor amplitud: {amplitudes[idx_max_amp]:.2f} el día {dias[idx_max_amp]}")

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

alumnos = 5
materias = 3

print("== Carga de notas (5 estudiantes x 3 materias) ==")
notas = []
for i in range(alumnos):
    fila = []
    for j in range(materias):
        valor = float(input(f"Nota del estudiante {i+1} en materia {j+1}: "))
        fila.append(valor)
    notas.append(fila)

print("\nPromedio por estudiante:")
for i, fila in enumerate(notas, start=1):
    prom = sum(fila) / materias
    print(f"Estudiante {i}: {prom:.2f}")

print("\nPromedio por materia:")
for j in range(materias):
    col = [notas[i][j] for i in range(alumnos)]
    prom = sum(col) / alumnos
    print(f"Materia {j+1}: {prom:.2f}")

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(t):
    for fila in t:
        print(" ".join(fila))
    print()

print("\n== Ta-Te-Ti ==")
mostrar_tablero(tablero)

jugador = "X" 
for turno in range(9):
    print(f"Turno {turno+1} - Juega '{jugador}'")
    try:
        f = int(input("Fila (1-3): ")) - 1
        c = int(input("Columna (1-3): ")) - 1
    except ValueError:
        print("Entrada inválida. Intentá de nuevo.")
        continue

    if not (0 <= f < 3 and 0 <= c < 3):
        print("Posición fuera de rango. Intentá de nuevo.")
        continue
    if tablero[f][c] != "-":
        print("Casilla ocupada. Elegí otra.")
        continue

    tablero[f][c] = jugador
    mostrar_tablero(tablero)

    # alternar jugador
    jugador = "O" if jugador == "X" else "X"

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(t):
    for fila in t:
        print(" ".join(fila))
    print()

print("\n== Ta-Te-Ti ==")
mostrar_tablero(tablero)

jugador = "X"
for turno in range(9):
    print(f"Turno {turno+1} - Juega '{jugador}'")
    try:
        f = int(input("Fila (1-3): ")) - 1
        c = int(input("Columna (1-3): ")) - 1
    except ValueError:
        print("Entrada inválida. Intentá de nuevo.")
        continue

    if not (0 <= f < 3 and 0 <= c < 3):
        print("Posición fuera de rango. Intentá de nuevo.")
        continue
    if tablero[f][c] != "-":
        print("Casilla ocupada. Elegí otra.")
        continue

    tablero[f][c] = jugador
    mostrar_tablero(tablero)

    jugador = "O" if jugador == "X" else "X"