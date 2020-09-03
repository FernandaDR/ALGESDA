import OrdenamientoBurbuja
import OrdenamientoInsercion
import time
import OrdenamientoMezcla
import random

size_list= int (input("Ingrese tamaño de la lista : "))
lista = [random.randint(500,2000) for i in range(size_list)]
lista_desordenada = lista
print("se muestra la lista desordenada")
print(lista_desordenada)
lista_desordenada_2 = lista
lista_desordenada_3 = lista

inicio = time.time()
OrdenamientoBurbuja.ordenamiento_burbuja(lista)
final_burbuja = time.time()-inicio

inicio = time.time()
OrdenamientoInsercion.ordenamiento_por_insercion(lista_desordenada)
final_insercion = time.time()-inicio

inicio = time.time()
OrdenamientoMezcla.ord_por_mezcla(lista_desordenada_2)
final_mezcla = time.time()-inicio

print("se muestra la lista ordenada")
print(lista_desordenada)
print(f"el tiempo final de burbuja es {final_burbuja} y el de insercion {final_insercion} y el tiempo final de mezcla {final_mezcla}")
print("La técnica de ordenamiento más eficiente es la de Inserción")