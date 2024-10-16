""" 
Ejercicio 1 Saca en Pantalla el Hola Mundo
print('Hola Mundo')
"""

"""
Ejercicio 1.1 Pide al usuario su nombre y luego imprime un saludo personalizado
nombre = input('Ingresa tu nombre: ')

print(f'Hola {nombre} me encanta tu nombre')
"""

"""
1.2 Calcula la suma de dos numeros ingresados por el usuario y muestra el resutado
n1 = input('Introduce el primer numero: ')
n2 = input('Introduce el segundo numero: ')

print(f'La suma de {n1} y {n2} es {int(n1) + int(n2)}')
"""


# Estructuras de control
"""
n1 = int(input('Introduce el primer numero: '))

if n1%2 == 0:
    print('Es par')

else:
    print('No es par')

"""
"""
n1 = int(input('Introduce el primer numero: '))

if n1 > 0:
    print('El numero es positivo')

else:
    if n1 < 0:
        print('El numero es negativo')
    else:
        print('El numero es igual a 0')
"""
"""
n1 = int(input('Introduce el primer numero: '))

if n1 > 0:
    print('El numero es positivo')
elif n1<0:
    print('El numero es negativo')
else:
    print('El numero es igual a 0')

"""


"""
suma = 0
for i in range(3):
    suma += int(input('Ingresa un numero: '))
    
print('El promedio de los numeros introducidos es: ', int(suma/3))
"""
"""
lista = ['Carlos', 'Marina', 'Paco', 'Javi']

for i in lista:
    print(i, end= " ")
"""

"""
lista = []

num = 1
while num != 0:
    lista.append(int(input('Introduce un número: ')))
    lista.append(num)



mayor = lista[0]
for n in range(1, lista.__len__()):
    if lista[n] > mayor:
        mayor = lista[n]

print('El mayor es ', mayor)

for n in lista:
    if n > mayor:
        mayor = n

"""

"""

import random

numero = random.randint(1,100)

fin = False


while fin == False:
    n = int(input('Introduce un numero: '))

    if n == numero:
        print('Enorabuena')
        fin = True
    elif n > numero:
        print('El numero es mas pequeño')
    else:
        print(' El numero es mas grande')

"""

"""
def areaTriangulo():
    base = int(input('Introduce la base del triangulo: '))
    altura = int(input('Introduce la altura del triangulo: '))
    return base*altura/2


print(int(areaTriangulo()))
"""


"""

def conversionGrados():
    celsius = int(input('Introduce los grados celsius: '))
    return celsius*9/5+32


print('\nLos grados farenheint son: ', int(conversionGrados()))
"""




# Escribe una función que determine si una palabra es un palíndromo (simétrica)



"""
def esPalindromo():
    palabra = input('Introduce la palabra para ver si es polindromo: ')
    for i in range(len(palabra)//2):
        if palabra[i] != palabra[len(palabra)-1 -i]:
            return False
        
    return True

        


if esPalindromo() == True:
    print('Es palindromo')
else:
    print('No es polindromo')
"""

# Factorial
"""
def calcularFactorial(n):
   f = 1
   for i in range(2,n+1):
        f *= i
   return f

print(calcularFactorial(5))
"""

"""
def factorialRec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorialRec(n-1)



print(factorialRec(5))
"""


def mostrarRec(pal, index):
    if index != len(pal):
        print(pal[index], end="")
        mostrarRec(pal, index + 1)



print(mostrarRec('Carlos',0))

