
#? Instalar numpy
#? pip install numpy

#? importando numpy, lo llamo con el alias np
import numpy as np
"""#! Arreglo de una dimension
arreglo_sin_numpy = [1,2,3,4,5,6,7,8]
arreglo = np.array([1,2,3,4,5,6,7,8])

print('lista sin numpy')
print (arreglo_sin_numpy)

print('Lista con Numpy')  #! no se imprimen las comas como es normal en la lista
print (arreglo)

#! Arreglo de 2 dimensiones

arreglo_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print ( arreglo_2d)

#! Arreglo de 3 dimensiones completada con ceros

arreglo_3d = np.zeros((3,3)) #? se pasa las dimensiones en forma de tuplas n filas y  n columnas
print(arreglo_3d)

#! Arreglo de 3 dimensions com"pletadas con unos
arreglos_con_1 = np.ones((2,4))
print(arreglos_con_1)

#! Arreglo en un rango, indicando el numero de inicio y salto, se pasa como lista los argumentos
arre_aleatorio = np.arange(0,10,2)
print (arre_aleatorio)"""

# CREAR UN ARRAY

"""arr = np.array([1,2,3,4,5,6,7,8,9,10])
arr_multiplicacion  =  arr * 2
print('Arreglo en el que se multiplica cada elemento por 2')
print(arr_multiplicacion)

print('********************')
print('Arreglo filtrado con valores mayores a 5')
arr_mayor5 =  arr[arr > 5 ]
print(arr_mayor5)"""

#? OPERACIONES BASICAS 
"""a = np.array([2,4,5,6])
b = np.array([2,1,2,4])
print('SUMA: ', a + b)
print('RESTA: ', a - b)
print('MULPTIPLICACION: ', a*b)
print('DIVISION: ', a/b)"""

"""arreglo_estadistico = (2,1,3,4,5,6,4,3,1,23,5,6,7,2,3,1)
media = np.mean(arreglo_estadistico)
print(media)"""

#! Manipulacion de arreglos de dos dimensiones
"""#? crear un array aleatorio de 3x3
arr_3d =  np.random.randint(1,10,(3,3))
#print(arr_3d)

#? acceder al elemento (1,2) del arreglo
elemento_a12 = arr_3d[1,2]
print(elemento_a12)

#? cambiar la 2 fila por ceros

fila2_cer0 = arr_3d[2,:] = 0 
print(fila2_cer0)

suma = np.sum(arr_3d)
print(suma)"""

#! crear un arreglo de 100 elementos entre 0 y 1
arreglo_random = np.random.rand(100)

suma = np.sum(arreglo_random)
promedio = np.mean(arreglo_random)
maximo_ = np.max(arreglo_random)
minimo_ =  np.min(arreglo_random)

print(suma)
print(promedio)
print (maximo_)
print(minimo_)