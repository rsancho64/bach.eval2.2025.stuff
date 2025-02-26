#! /usr/bin/python3

# function echo
def echo(algo):
    return algo

respuesta = echo("Hello World")
print(respuesta)

print (echo("Hello World"))
 
# siguiente
def siguienteDe(numero):
    return numero + 1

numero = 55
print(siguienteDe(numero))

n = 666
print(f"el siguiente de {n} es {siguienteDe(n)}")

def sumaDosCosas(a, b):
    return a + b    

print(sumaDosCosas(2, 3))
print(sumaDosCosas("hola", " mundo"))

def dobleDe(numero):
    return numero * 2

# manejando listas
# una funcion que recibe una lista 
# y la devuelve con el doble de cada elemento 
def dobleDeCadaElemento(lista):
    nuevaLista = []
    for elemento in lista:
        nuevoElemento = dobleDe(elemento)
        nuevaLista.append(nuevoElemento)
    return nuevaLista

lista = [1, 2, 3, 4, 5]
print(lista)
print(dobleDeCadaElemento(lista))

otralista = ["hola", "mundo", "cruel"]
print(otralista)
print(dobleDeCadaElemento(otralista))