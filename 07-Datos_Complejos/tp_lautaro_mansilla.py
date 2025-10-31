from __future__ import annotations
from collections import Counter
import string

# Ejercicio 1
# Diccionario precios_frutas: agregar elementos
def punto1_precios_frutas() -> dict[str, int]:
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    nuevos = {'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
    precios_frutas.update(nuevos)
    return precios_frutas


# Ejercicio 2
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana a 1330, Manzana a 1700 y Melón a 2800.
def punto2_actualizar_precios(precios_frutas: dict[str, int]) -> dict[str, int]:
    actualizaciones = {'Banana': 1330, 'Manzana': 1700, 'Melón': 2800}
    precios_frutas.update(actualizaciones)
    return precios_frutas


# Ejercicio 3
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios
def punto3_lista_solo_frutas(precios_frutas: dict[str, int]) -> list[str]:
    return list(precios_frutas.keys())


# Ejercicio 4
# Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.
def punto4_agenda_telefonica() -> None:
    print("\n[Punto 4] Agenda telefónica")
    contactos: dict[str, str] = {}
    for i in range(1, 6):
        nombre = input(f"  Ingresá el nombre #{i}: ").strip()
        numero = input(f"  Ingresá el número de {nombre}: ").strip()
        contactos[nombre] = numero

    consulta = input("  Consultá un nombre para ver su número: ").strip()
    numero = contactos.get(consulta)
    if numero:
        print(f"  => {consulta}: {numero}")
    else:
        print("  => No existe ese contacto.")


# Ejercicio 5
# Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
def normalizar_texto(frase: str) -> list[str]:
    # Minúsculas y elimina puntuación común (incluye signos españoles)
    tabla = str.maketrans("", "", string.punctuation + "¡!¿?""'""«»…")
    palabras = frase.lower().translate(tabla).split()
    return palabras


def punto5_analizar_frase() -> None:
    print("\n[Punto 5] Análisis de frase")
    frase = input("  Ingresá una frase: ")
    palabras = normalizar_texto(frase)
    unicas = set(palabras)
    conteo = Counter(palabras)
    print("  Palabras únicas:", unicas)
    print("  Frecuencia:", dict(conteo))


# Ejercicio 6
# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
def punto6_promedios_alumnos() -> None:
    print("\n[Punto 6] Promedios de alumnos")
    alumnos: dict[str, tuple[float, float, float]] = {}
    for i in range(1, 4):
        nombre = input(f"  Nombre del alumno #{i}: ").strip()
        n1 = float(input("   Nota 1: "))
        n2 = float(input("   Nota 2: "))
        n3 = float(input("   Nota 3: "))
        alumnos[nombre] = (n1, n2, n3)

    print("  Promedios:")
    for nombre, notas in alumnos.items():
        prom = sum(notas) / 3.0
        print(f"   - {nombre}: {prom:.2f}")


# Ejercicio 7
# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
def leer_set_estudiantes(etiqueta: str) -> set[str]:
    print(f"  Ingresá nombres aprobados de {etiqueta} separados por coma (ej: Ana,Juan,Lu):")
    linea = input("   > ").strip()
    if not linea:
        return set()
    return {nombre.strip() for nombre in linea.split(",") if nombre.strip()}


def punto7_resumen_aprobados() -> None:
    print("\n[Punto 7] Resumen de aprobados")
    p1 = leer_set_estudiantes("Parcial 1")
    p2 = leer_set_estudiantes("Parcial 2")

    ambos = p1 & p2
    solo_uno = p1 ^ p2
    al_menos_uno = p1 | p2

    print("  Aprobados en ambos:", ambos)
    print("  Aprobados solo en uno:", solo_uno)
    print("  Aprobados en al menos uno:", al_menos_uno)


# Ejercicio 8
# Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe
def punto8_gestionar_stock() -> None:
    print("\n[Punto 8] Gestión de stock")
    stock: dict[str, int] = {"mouse": 10, "teclado": 5, "monitor": 2}

    while True:
        print("\n  Opciones: [C]onsultar / [A]gregar unidades / [N]uevo producto / [S]alir")
        op = input("   > ").strip().lower()

        if op == "c":
            prod = input("   Producto a consultar: ").strip().lower()
            print(f"   Stock de {prod}: {stock.get(prod, 0)}")
        elif op == "a":
            prod = input("   Producto existente: ").strip().lower()
            if prod in stock:
                try:
                    unidades = int(input("   Unidades a agregar: "))
                except ValueError:
                    print("   Valor no válido.")
                    continue
                stock[prod] += max(0, unidades)
                print(f"   Actualizado: {prod} = {stock[prod]}")
            else:
                print("   Ese producto no existe. Usá 'N' para crearlo.")
        elif op == "n":
            prod = input("   Nuevo producto: ").strip().lower()
            try:
                unidades = int(input("   Unidades iniciales: "))
            except ValueError:
                print("   Valor no válido.")
                continue
            stock[prod] = max(0, unidades)
            print(f"   Creado: {prod} = {stock[prod]}")
        elif op == "s":
            print("   Saliendo de gestión de stock. Estado final:", stock)
            break
        else:
            print("   Opción inválida.")


# Ejercicio 9
# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos Permití consultar qué actividad hay en cierto día y hora.
def punto9_agenda_eventos() -> None:
    print("\n[Punto 9] Agenda de eventos")
    agenda: dict[tuple[str, str], str] = {}

    while True:
        print("\n  Opciones: [A]gregar evento / [Q]uerie (consulta) / [S]alir")
        op = input("   > ").strip().lower()

        if op == "a":
            dia = input("   Día (ej: Lunes): ").strip().title()
            hora = input("   Hora (HH:MM): ").strip()
            evento = input("   Evento: ").strip()
            agenda[(dia, hora)] = evento
            print("   Guardado.")
        elif op == "q":
            dia = input("   Día (ej: Lunes): ").strip().title()
            hora = input("   Hora (HH:MM): ").strip()
            print("   =>", agenda.get((dia, hora), "No hay actividad en ese día y hora."))
        elif op == "s":
            print("   Saliendo. Agenda final:", agenda)
            break
        else:
            print("   Opción inválida.")


# Ejercicio 10
# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores
def punto10_invertir_paises_capitales() -> None:
    print("\n[Punto 10] Inversión país->capital a capital->país")
    print("  Cargá pares país:capital separados por coma. Ej: Argentina:Buenos Aires, Francia:París")
    linea = input("   > ").strip()
    pares = [p.strip() for p in linea.split(",") if p.strip()]
    pais_a_capital: dict[str, str] = {}
    for par in pares:
        if ":" in par:
            pais, capital = [x.strip() for x in par.split(":", 1)]
            if pais and capital:
                pais_a_capital[pais] = capital

    invertido = {capital: pais for pais, capital in pais_a_capital.items()}
    print("  Diccionario invertido (capital -> país):", invertido)
