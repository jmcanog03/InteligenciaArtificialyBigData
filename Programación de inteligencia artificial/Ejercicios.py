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

"""
def mostrarRec(pal, index):
    if index != len(pal):
        print(pal[index], end="")
        mostrarRec(pal, index + 1)



print(mostrarRec('Carlos',0))
"""


        
"""
class Persona:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion


p = Persona('Carlos', 28, 'Calle Miguel de Cervantes nº31')

print(p.edad)
        
"""

#Crea una clase llamada "Rectángulo" con atributos para el ancho y el alto. Agrega métodos para calcular el área y el perímetro del rectángulo



"""
class Rectangulo:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
    
    def calcularArea(self):
        return self.alto*self.ancho
    
    def calcularPerimetro(self):
        return self.alto*2 + self.ancho*2


r = Rectangulo(10,4)

print(f'El área del rectangulo es {r.calcularArea()} y el perímetro es {r.calcularPerimetro()}')
"""


class Contacto:
    def __init__(self, nombre, telefono, direccion, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
    
    def __str__(self):
        return f'Me llamo {self.nombre}, mi telefono es {self.telefono}'


def buscarContacto(lista):
    l = list(lista)

    for Contacto in lista:
        if Contacto.nombre == 'María':
            print(Contacto)

    




agenda = [
    Contacto('Josema', 600332454, 'Miguel de Cervantes', 'josema@gmail.com'),
    Contacto('Ana', 610123456, 'Calle Mayor', 'ana@hotmail.com'),
    Contacto('Luis', 620987654, 'Avenida del Sol', 'luis@gmail.com'),
    Contacto('María', 630555111, 'Plaza de España', 'maria@yahoo.com'),
    Contacto('Carlos', 640222333, 'Calle Luna', 'carlos@gmail.com'),
    Contacto('Elena', 650444555, 'Avenida del Parque', 'elena@hotmail.com'),
    Contacto('Pedro', 660666777, 'Calle Las Flores', 'pedro@gmail.com'),
    Contacto('Laura', 670888999, 'Paseo del Río', 'laura@yahoo.com'),
    Contacto('Javier', 680111222, 'Calle del Olmo', 'javier@gmail.com'),
    Contacto('Carmen', 690333444, 'Calle del Prado', 'carmen@hotmail.com')
]


buscarContacto(agenda)