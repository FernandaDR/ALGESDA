  
import BusquedaBinaria
import BusquedaLineal
import time

def resultado (encontrado):
    if encontrado == True:
        print("Encontraron el nùmero")
    else:
        print ("El numero no existe en la lista")

lista = BusquedaLineal.crear_lista()
print(lista)
lista_ordenada = sorted(lista)
numero = int (input ("ingrese número objetivo : "))
comienzo = time.time()
resultado1 = BusquedaLineal.busqueda_lineal(lista,numero)
resultado(resultado1)
print (f"tiempo de busqueda lineal {time.time()-comienzo} en segundos")
comienzo = time.time()
resultado2 = BusquedaBinaria.busqueda_binaria(lista_ordenada,0,len(lista_ordenada), numero)
print (f"tiempo de busqueda bineria {time.time()-comienzo} en segundos")
resultado(resultado2)