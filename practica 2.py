
# Estructuras Iterativas

# Problema 1: 
# Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5, 
# en el rango de 1500 y 2700 (ambos incluidos). 

for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num, end=", ")

# Problema 2: 
#Escriba un programa en Python para construir el siguiente patrón. 

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

for i in range(1, 6):
    print("* " * i)

for i in range(4, 0, -1):
    print("* " * i)

# Problema 3: 
# Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El 
# ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos 
# números. 

# Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de 
# números pares e impares.

numeros = []

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").strip().upper()
    if respuesta == "NO":
        break
    elif respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)

# Contar pares e impares
pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Números ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)

# Problema 4: 
# Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se 
# pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus 
# materias.

alumnos = []

n = int(input("¿Cuántos alumnos desea registrar?: "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumno = {"Alumno": nombre, "Notas": notas}
    alumnos.append(alumno)

print("\nListado de alumnos:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

# Funciones:

# Problema 5: 
# Genere una función que tenga como parámetros el ingreso de un número entero y un dígito. 
# Verifique la cantidad de veces que se usa dicho número en el dígito solicitado. 

def contar_digito(numero, digito):
    numero_str = str(numero)
    digito_str = str(digito)

    cantidad = numero_str.count(digito_str)
    return cantidad

numero_ingresado = int(input("Ingrese un número entero: "))
digito_ingresado = input("Ingrese el dígito que desea contar: ")

if digito_ingresado.isdigit() and len(digito_ingresado) == 1:
    resultado = contar_digito(numero_ingresado, digito_ingresado)
    print(f"El dígito '{digito_ingresado}' aparece {resultado} veces en el número {numero_ingresado}.")
else:
    print("Debe ingresar un solo dígito válido (0-9).")

# Problema 6: 
# Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50. 
# Nota: La secuencia de Fibonacci es la serie de números: 
# 0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
# Cada número siguiente se obtiene sumando los dos números anteriores. 

def serie_fibonacci_hasta_50():
    a, b = 0, 1
    print("Serie de Fibonacci entre 0 y 50:")
    while a <= 50:
        print(a, end=" ")
        a, b = b, a + b
    print()  # salto de línea al final

serie_fibonacci_hasta_50()

# Problema 7: 
# Escriba una función de Python que tome un número como parámetro y verifique que el número sea 
# primo o no. 

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

num = int(input("Ingrese un número para verificar si es primo: "))
if es_primo(num):
    print(f"El número {num} es primo.")
else:
    print(f"El número {num} NO es primo.")

# Problema 8: 
# Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La 
# función acepta el número como argumento. 

def calcular_factorial(n):
    if n < 0:
        return None  # El factorial no está definido para negativos
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

num = int(input("Ingrese un número entero no negativo para calcular su factorial: "))
if num < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = calcular_factorial(num)
    print(f"El factorial de {num} es: {resultado}")

# Métodos de Cadenas:

# Problema 9: 
# Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio, 
# por ejemplo, omitiendo las vocales. 
# Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo 
# texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o 
# minúsculas.

def eliminar_vocales(texto):
    vocales = "aeiouAEIOU"
    resultado = ""
    for caracter in texto:
        if caracter not in vocales:
            resultado += caracter
    return resultado

entrada = input("Ingrese un texto para eliminar las vocales: ")
salida = eliminar_vocales(entrada)
print(f"Texto sin vocales: {salida}")

# Problema 10: 
# En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las 
# fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en 
# lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente 
# en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son 
# ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de 
# 1636! 

# Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como 
# 8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en 
# la lista abajo: 

# [ 
#    "Enero", 
#   "Febrero", 
#    "Marzo", 
#    "Abril", 
#    "Mayo", 
#    "Junio", 
#    "Julio", 
#    "Agosto", 
#    "Septiembre", 
#    "Octubre", 
#    "Noviembre", 
#    "Diciembre" 
# ] 
 
# Luego, genere esa misma fecha en formato AAAA-MM-DD.

def convertir_fecha(fecha):
    meses = {
        "Enero": "01", "Febrero": "02", "Marzo": "03", "Abril": "04",
        "Mayo": "05", "Junio": "06", "Julio": "07", "Agosto": "08",
        "Septiembre": "09", "Octubre": "10", "Noviembre": "11", "Diciembre": "12"
    }

    try:
        if "/" in fecha:
            mes, dia, anio = fecha.split("/")
            mes = mes.zfill(2)
            dia = dia.zfill(2)
        else:
            partes = fecha.replace(",", "").split()
            mes = meses.get(partes[0].capitalize())
            dia = partes[1].zfill(2)
            anio = partes[2]

        return f"{anio}-{mes}-{dia}"
    except:
        return "Formato inválido. Intente nuevamente."

entrada = input("Ingrese una fecha (MM/DD/AAAA o 'Mes D, AAAA'): ")
salida = convertir_fecha(entrada)
print(f"Fecha en formato AAAA-MM-DD: {salida}")













