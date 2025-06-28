
#  VARIABLES

#  Problema 1:
#  Escribir un programa que solicite su nombre de usuario por consola y después de que el usuario lo
# introduzca muestre por pantalla la cadena “¡Hola <nombre>!”, donde <nombre> es el nombre que el
# usuario haya introducido.

nombre = input("Introduce tu nombre: ")

print(f"¡Hola {nombre}!")

#Problema 2:
# En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
# restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
# Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
# porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
# dejar como propina.

consumo = float(input("¿Cuánto fue el consumo en el restaurante? S/: "))

porcentaje = float(input("¿Qué porcentaje de propina deseas dejar? %: "))

propina = (porcentaje / 100) * consumo

print(f"La propina que debes dejar es: S/ {propina:.2f}")

#Problema 3:
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
# por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
# peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
# cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
# último pedido y calcule el peso total del paquete que será enviado.

peso_payaso = 112
peso_muneca = 75

numero_payasos = int(input("¿Cuántos payasos se vendieron?: "))
numero_munecas = int(input("¿Cuántas muñecas se vendieron?: "))

peso_total = (numero_payasos * peso_payaso) + (numero_munecas * peso_muneca)

print(f"El peso total del paquete es: {peso_total} gramos")

# Problema 4:
# Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
# pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
# puede ser calculada de la siguiente forma:

n = int(input("Introduce un número entero positivo: "))

suma = n * (n + 1) // 2  # Usamos // para asegurar un resultado entero

print(f"La suma de los primeros {n} números enteros positivos es: {suma}")

#  CONDICIONALES

# Problema 5:
# Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
# último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
# verdad (True o False  - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows

shows_vistos = int(input("¿Cuántos shows musicales has visto en el último año? "))

ha_visto_mas_de_tres = shows_vistos > 3

print("¿Has visto más de 3 shows musicales?", ha_visto_mas_de_tres)

#  Problema 6:
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
# calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
# preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
# años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.

edad = int(input("¿Cuál es tu edad? "))

if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 5
else:
    precio = 10

print(f"El precio de tu entrada es: ${precio}")

# Problema 7:
# Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

print("\nElige una opción del menú:")
print("1. Sumar los dos números")
print("2. Restar el segundo al primero")
print("3. Multiplicar los dos números")

opcion = input("Introduce el número de la opción (1, 2 o 3): ")

if opcion == "1":
    resultado = numero1 + numero2
    print(f"La suma es: {resultado}")
elif opcion == "2":
    resultado = numero1 - numero2
    print(f"La resta es: {resultado}")
elif opcion == "3":
    resultado = numero1 * numero2
    print(f"La multiplicación es: {resultado}")
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")

# Problema 8:
# Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
# entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
# Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
# hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
# Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
# suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
# las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.

time = input("Ingrese la hora (formato 24 horas, ej. 7:30 o 12:00): ")

horas, minutos = time.split(":")

horas = int(horas)
minutos = int(minutos)

if (horas == 7) or (horas == 8 and minutos == 0):
    print("Es hora del desayuno.")

elif (horas == 12) or (horas == 13 and minutos == 0):
    print("Es hora del almuerzo.")

elif (horas == 18) or (horas == 19 and minutos == 0):
    print("Es hora de la cena.")

# COLECCIONES DE DATOS

#  Problema 9:
# Escriba un programa que, dada una lista, devuelve una nueva lista cuyo contenido sea igual a la
# original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a',
# 'día', 'buen', 'Di'].

lista = ['Di', 'buen', 'día', 'a', 'papa']

lista_invertida = lista[::-1]

print("Lista invertida:", lista_invertida)

# Problema 10:
# Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
# encuentran en la posición 0, 4 y 5.
# lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
# Resultado esperado: ['Verde', 'Blanco', 'Negro'

lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

lista_filtrada = [valor for i, valor in enumerate(lista) if i not in (0, 4, 5)]

print("Lista filtrada:", lista_filtrada)

#Problema 11:
# Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente
# lista. Su programa debe retornar otra lista sin los duplicados.
# Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
# Lista procesada: [1, 2, 3, 4, 5]

lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

lista_sin_duplicados = []
for elemento in lista_original:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)

print("Lista sin duplicados:", lista_sin_duplicados)

#  Problema 12:
# La mayoría de los archivos tienen extensiones de archivo, el cual es un sufijo que comienza con un
# punto (.) al final de su nombre. Por ejemplo, los nombres de archivo para GIF terminan en .gif y los
# nombres de archivo para JPEG terminan en .jpg o .jpeg. Mientras que en los sistemas operativos
# como Windows, el tipo de archivo le sirve al computador abrir el archivo en el formato apropiado, en
# la web esto es distinto.  Los navegadores web, por el contrario, se basan en tipos de medios,
# anteriormente conocidos como tipos MIME, para determinar cómo mostrar los archivos que viven en
# la web. Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de
# archivo MIME correspondiente. Si el nombre del archivo termina en cualquiera de estos sufijos (sin
# importar el uso de mayúsculas y minúsculas) 
#.gif
#.jpg
#.jpeg
#.png
#.pdf
#.txt
#.zip
# Si el nombre del archivo termina con algún otro sufijo que no se encuentra en la lista o no tiene
# ningún sufijo, en su lugar su programa deberá devolver application/octet-stream.

nombre_archivo = input("Introduce el nombre del archivo: ").strip().lower()

tipos_mime = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

for extension, tipo in tipos_mime.items():
    if nombre_archivo.endswith(extension):
        print(tipo)
        break
else:
    print("application/octet-stream")

