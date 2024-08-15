import numpy as np

#? datos de la venta durante 5 años
ventas = np.random.randint(500,2000,(5,12)) #? 5 son los años y 12 los meses
print(ventas)

#? calcular el total de ventas por producto
total_venta_producto = np.sum(ventas, axis= 1) # el axis especifica la suma por FILA
#print(total_venta_producto)

#? indentificar el mes con mayores ventas para cada producto
maximo_mes_venta =  np.argmax(ventas, axis= 1) #! devuelve el indice del maximo valor de cada FILA
print('')
#print(maximo_mes_venta)

#? calcular el promedio mensual de ventas por producto
promedio_ventas_producto = np.mean(ventas, axis= 1)
print('')
#print(promedio_ventas_producto)

#? generar un array que contenga la diferencia porcentual de ventas entre meses consecutivo
diferencia_porcentual = (np.diff(ventas, axis= 1)/ventas[:,:-1])*100

print(diferencia_porcentual)