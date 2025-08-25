#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla 
#“Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
pais = input("Ingres lugar de residencia:")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

import math 

radio = float(input("Por favor, ingrese el radio del círculo: "))

area = math.pi * radio**2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro (circunferencia) es: {perimetro:.2f}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Ingresa la cantidad de segundos: "))

horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas:.2f} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingresa un número: "))

n1 = numero * 1
n2 = numero * 2
n3 = numero * 3
n4 = numero * 4
n5 = numero * 5
n6 = numero * 6
n7 = numero * 7
n8 = numero * 8
n9 = numero * 9
n10 = numero * 10

print(f"{numero} x 1 = {n1}")
print(f"{numero} x 2 = {n2}")
print(f"{numero} x 3 = {n3}")
print(f"{numero} x 4 = {n4}")
print(f"{numero} x 5 = {n5}")
print(f"{numero} x 6 = {n6}")
print(f"{numero} x 7 = {n7}")
print(f"{numero} x 8 = {n8}")
print(f"{numero} x 9 = {n9}")
print(f"{numero} x 10 = {n10}")


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = round(num1 / num2)  


print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multiplicacion}")
print(f"La división es: {division}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = (9/5) * celsius + 32

print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio dedichos números.
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))

# Calcular el promedio
promedio = (n1 + n2 + n3) / 3

# Mostrar el resultado
print(f"El promedio de los tres números es: {promedio:.2f}")