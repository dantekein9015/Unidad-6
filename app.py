# TP 7 - Recursividad - UTN A Distancia
# Alumno: Enrique Alejandro Juarez Alvarez

# 1. Factorial recursivo
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# Pedir número al usuario
limite = int(input("Ingresá un número para ver los factoriales hasta ese valor: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

# 2. Serie de Fibonacci recursiva
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

tope = int(input("¿Hasta qué posición querés la serie de Fibonacci? "))
for i in range(tope):
    print(f"F({i}) = {fibonacci(i)}")

# 3. Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("Base: "))
exponente = int(input("Exponente: "))
print(f"{base}^{exponente} =", potencia(base, exponente))

# 4. Conversión decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

numero_decimal = int(input("Número decimal a convertir: "))
binario = decimal_a_binario(numero_decimal)
print("Binario:", binario if binario else "0")

# 5. Verificar si una palabra es palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Ingresá una palabra para verificar si es palíndromo: ").lower()
print("¿Es palíndromo?", es_palindromo(palabra))

# 6. Suma de dígitos (sin strings)
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

n = int(input("Número entero positivo para sumar sus dígitos: "))
print("Suma de dígitos:", suma_digitos(n))

# 7. Contar bloques en una pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

nivel = int(input("Cantidad de bloques en la base: "))
print("Total de bloques necesarios:", contar_bloques(nivel))

# 8. Contar cuántas veces aparece un dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    return contar_digito(numero // 10, digito)

numero = int(input("Número para analizar: "))
digito = int(input("¿Qué dígito querés contar (0-9)? "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")
