# ============================================================================
# EJERCICIO 1 - Factorial recursivo
# ============================================================================

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0 or n == 1:  # Caso base
        return 1
    return n * factorial(n - 1)  # Caso recursivo


def mostrar_factoriales(limite: int) -> None:
    print(f"\nFactoriales desde 1 hasta {limite}:")
    for i in range(1, limite + 1):
        print(f"  {i}! = {factorial(i)}")


# ============================================================================
# EJERCICIO 2 - Serie de Fibonacci recursiva
# ============================================================================

def fibonacci(pos: int) -> int:
    if pos < 0:
        raise ValueError("La posición debe ser un número no negativo")
    if pos == 0:  # Caso base
        return 0
    if pos == 1:  # Caso base
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)  # Caso recursivo


def mostrar_fibonacci(n: int) -> None:
    print(f"\nSerie de Fibonacci hasta la posición {n}:")
    for i in range(n + 1):
        print(f"  fibonacci({i}) = {fibonacci(i)}")


# ============================================================================
# EJERCICIO 3 - Potencia recursiva
# ============================================================================

def potencia(base: int | float, exponente: int) -> int | float:
    if exponente < 0:
        raise ValueError("Esta función solo acepta exponentes no negativos")
    if exponente == 0:  # Caso base
        return 1
    return base * potencia(base, exponente - 1)  # Caso recursivo


# ============================================================================
# EJERCICIO 4 - Conversión decimal a binario (recursivo)
# ============================================================================

def decimal_a_binario(n: int) -> str:
    if n < 0:
        raise ValueError("Solo se aceptan números positivos")
    if n == 0:  # Caso base
        return "0"
    if n == 1:  # Caso base
        return "1"
    # Caso recursivo: concatenar resultado de n//2 con el resto
    return decimal_a_binario(n // 2) + str(n % 2)


# ============================================================================
# EJERCICIO 5 - Palíndromo recursivo
# ============================================================================

def es_palindromo(palabra: str) -> bool:
    # Caso base: palabra vacía o de un solo carácter
    if len(palabra) <= 1:
        return True
    
    # Caso recursivo: comparar primer y último carácter
    if palabra[0] != palabra[-1]:
        return False
    
    # Verificar la subcadena interna
    return es_palindromo(palabra[1:-1])


# ============================================================================
# EJERCICIO 6 - Suma de dígitos recursiva (sin strings)
# ============================================================================

def suma_digitos(n: int) -> int:
    if n < 0:
        n = abs(n)  # Trabajar con valor absoluto si es negativo
    
    if n < 10:  # Caso base
        return n
    
    # Caso recursivo: último dígito + suma del resto
    return (n % 10) + suma_digitos(n // 10)


# ============================================================================
# EJERCICIO 7 - Pirámide de bloques recursiva
# ============================================================================

def contar_bloques(n: int) -> int:
    if n <= 0:
        raise ValueError("El número de bloques debe ser positivo")
    
    if n == 1:  # Caso base
        return 1
    
    # Caso recursivo: bloques del nivel actual + bloques de niveles superiores
    return n + contar_bloques(n - 1)


# ============================================================================
# EJERCICIO 8 - Contar dígito en un número (recursivo)
# ============================================================================

def contar_digito(numero: int, digito: int) -> int:
    if digito < 0 or digito > 9:
        raise ValueError("El dígito debe estar entre 0 y 9")
    
    if numero < 0:
        numero = abs(numero)  # Trabajar con valor absoluto
    
    # Caso base: si el número es 0
    if numero == 0:
        # Si estamos buscando el 0 y el número es 0, cuenta como 1
        return 1 if digito == 0 else 0
    
    # Caso recursivo
    ultimo_digito = numero % 10
    resto = numero // 10
    
    # Si el último dígito coincide, sumar 1
    if ultimo_digito == digito:
        return 1 + contar_digito(resto, digito)
    else:
        return contar_digito(resto, digito)