import os

ARCHIVO_PRODUCTOS = "productos.txt"


def crear_archivo_inicial():
    """
    Crea el archivo productos.txt con 3 productos iniciales si no existe.
    """
    if not os.path.exists(ARCHIVO_PRODUCTOS):
        with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo:
            archivo.write("Lapicera,120.5,30\n")
            archivo.write("Cuaderno,500,10\n")
            archivo.write("Goma,90,50\n")
        print(f"Archivo '{ARCHIVO_PRODUCTOS}' creado con productos iniciales.\n")
    else:
        print(f"Archivo '{ARCHIVO_PRODUCTOS}' ya existe.\n")


def leer_archivo():
    """
    Lee el archivo productos.txt y retorna una lista de diccionarios.
    Cada diccionario contiene: nombre, precio, cantidad.
    """
    productos = []
    
    with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()  # Eliminar espacios y saltos de línea
            if linea:  # Verificar que la línea no esté vacía
                datos = linea.split(",")  # Separar por comas
                if len(datos) == 3:
                    producto = {
                        "nombre": datos[0],
                        "precio": float(datos[1]),
                        "cantidad": int(datos[2])
                    }
                    productos.append(producto)
    
    return productos


def mostrar_productos(productos):
    """
    Muestra todos los productos en el formato especificado.
    Formato: Producto: nombre | Precio: $precio | Cantidad: cantidad
    """
    print("=" * 60)
    print("LISTA DE PRODUCTOS")
    print("=" * 60)
    
    if not productos:
        print("No hay productos para mostrar.")
    else:
        for producto in productos:
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
    
    print("=" * 60)
    print()


def agregar_producto(productos):
    """
    Solicita datos al usuario para agregar un nuevo producto.
    Valida las entradas y agrega el producto al archivo y a la lista.
    """
    print("AGREGAR NUEVO PRODUCTO")
    print("-" * 60)
    
    # Pedir y validar nombre
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            break
        else:
            print("Error: El nombre no puede estar vacío. Intente nuevamente.")
    
    # Pedir y validar precio
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            print("Error: El precio debe ser un número válido. Intente nuevamente.")
    
    # Pedir y validar cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            break
        except ValueError:
            print("Error: La cantidad debe ser un número entero válido. Intente nuevamente.")
    
    # Agregar al archivo en modo append (sin borrar contenido existente)
    with open(ARCHIVO_PRODUCTOS, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    
    # Agregar a la lista en memoria
    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    productos.append(nuevo_producto)
    
    print(f"\nProducto '{nombre}' agregado correctamente.\n")


def buscar_producto(productos):
    """
    Busca un producto por nombre en la lista de productos.
    Muestra sus datos si existe, o un mensaje de error si no existe.
    """
    print("BUSCAR PRODUCTO")
    print("-" * 60)
    
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
    
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print("\nProducto encontrado:")
            print(f"  Nombre: {producto['nombre']}")
            print(f"  Precio: ${producto['precio']}")
            print(f"  Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    
    if not encontrado:
        print("\nEl producto no existe.")
    
    print()


def guardar_productos(productos):
    """
    Guarda todos los productos de la lista en el archivo productos.txt.
    Sobrescribe el archivo completo (modo 'w').
    """
    with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    
    print("Productos guardados correctamente en el archivo.\n")


def main():
    """
    Función principal que orquesta el flujo del programa.
    """
    print("\n" + "=" * 60)
    print("  SISTEMA DE GESTION DE PRODUCTOS")
    print("=" * 60 + "\n")
    
    # 1. Crear archivo inicial si no existe
    crear_archivo_inicial()
    
    # 2. Leer productos del archivo (cargar en lista de diccionarios)
    productos = leer_archivo()
    
    # 3. Mostrar productos
    mostrar_productos(productos)
    
    # 4. Agregar un producto desde teclado
    agregar_producto(productos)
    
    # 5. Mostrar productos actualizados
    print("PRODUCTOS DESPUES DE AGREGAR:")
    mostrar_productos(productos)
    
    # 6. Buscar producto por nombre
    buscar_producto(productos)
    
    # 7. Guardar productos actualizados en el archivo
    guardar_productos(productos)
    
    print("=" * 60)
    print("  Programa finalizado correctamente")
    print("=" * 60 + "\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()