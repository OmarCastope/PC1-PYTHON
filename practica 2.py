
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





# Problema 6: 
# Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50. 
# Nota: La secuencia de Fibonacci es la serie de números: 
# 0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
# Cada número siguiente se obtiene sumando los dos números anteriores. 



# Problema 7: 
# Escriba una función de Python que tome un número como parámetro y verifique que el número sea 
# primo o no. 


# Problema 8: 
# Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La 
# función acepta el número como argumento. 


# Métodos de Cadenas:

# Problema 9: 
# Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio, 
# por ejemplo, omitiendo las vocales. 
# Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo 
# texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o 
# minúsculas.






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















