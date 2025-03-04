#! /usr/bin/python3

def echo(algo):
    """Esta funcion recibe algo y lo devuelve"""
    return algo

def siguienteDe(numero):
    """Esta funcion recibe un numero? y devuelve el siguiente"""
    return numero + 1

def sumaDosCosas(a, b):
    """Esta funcion recibe dos cosas y calcula y retorna su suma
    es polimorfica, 
    el tipo de salida depende del tipo de los datos de la entrada"""
    return a + b    

def dobleDe(numero):
    """Esta funcion recibe una cosa y calcula y retorna el doble de su valor
    es polimorfica, el tipo de salida depende del tipo de entrada"""    
    return numero * 2

# manejando listas

def dobleDeCadaElemento(lista):
    """funcion que recibe una lista 
    y devuelve otra igual de larga con 
    los elementos doblados """ 

    nuevaLista = []
    for elemento in lista:
        nuevoElemento = dobleDe(elemento)
        nuevaLista.append(nuevoElemento)
    return nuevaLista


if __name__ == "__main__":

    respuesta = echo("Hello World")
    print(respuesta)

    print (echo("Hello World"))
 
    numero = 55
    print(siguienteDe(numero))

    n = 666
    print(f"el siguiente de {n} es {siguienteDe(n)}")

    print(sumaDosCosas(2, 3))
    print(sumaDosCosas("hola", " mundo"))

    lista = [1, 2, 3, 4, 5]
    print(lista)
    print(dobleDeCadaElemento(lista))

    otralista = ["hola", "mundo", "cruel"]
    print(otralista)
    print(dobleDeCadaElemento(otralista))
  
# FUNCIONES: ------------------------ 
# def echo(algo):
# def siguienteDe(numero):
# def sumaDosCosas(a, b):
# def dobleDe(numero):
# def dobleDeCadaElemento(lista):

# SALIDA: -----------------------------
# Hello World
# Hello World
# 56
# el siguiente de 666 es 667
# 5
# hola mundo
# [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]
# ['hola', 'mundo', 'cruel']
# ['holahola', 'mundomundo', 'cruelcruel']
# ---------------------------------------

# FUNCIONES POR HACER: ----------------

def anteriorDe(numero):
    return numero - 1

def sumaLosDoblesDeLosElementosEn(lista):
    total = 0
    for elemento in lista:
        total += dobleDe(elemento) 
    return total   

print (f"suma de valores doblados" +
       f" en la lista {lista}" + 
       f" es {sumaLosDoblesDeLosElementosEn(lista)}"
       )

# salida:
# suma de valores doblados en [1, 2, 3, 4, 5] es 30

def sumaTresCosas(a, b, c):
    return a + b + c


