#! /usr/bin/python3


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
    
    def inorder(self):
        if self.raiz:
            self._inorder_recursivo(self.raiz)
            print()
    
    def _inorder_recursivo(self, nodo):
        if nodo:
            self._inorder_recursivo(nodo.izquierda)
            print(nodo.valor, end=" ")
            self._inorder_recursivo(nodo.derecha)
    
    def preorder(self):
        if self.raiz:
            self._preorder_recursivo(self.raiz)
            print()
    
    def _preorder_recursivo(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self._preorder_recursivo(nodo.izquierda)
            self._preorder_recursivo(nodo.derecha)
    
    def postorder(self):
        if self.raiz:
            self._postorder_recursivo(self.raiz)
            print()
    
    def _postorder_recursivo(self, nodo):
        if nodo:
            self._postorder_recursivo(nodo.izquierda)
            self._postorder_recursivo(nodo.derecha)
            print(nodo.valor, end=" ")

class ManejadorConsola:
    def __init__(self):
        self.arbol = ArbolBinario()
        self.comandos = {
            'agregar': self.agregar,
            'inorder': self.inorder,
            'preorder': self.preorder,
            'postorder': self.postorder,
            'ayuda': self.ayuda,
            'salir': self.salir
        }
    
    def agregar(self, args):
        try:
            valor = int(args[0])
            self.arbol.insertar(valor)
            print(f"Valor {valor} agregado al árbol")
        except (IndexError, ValueError):
            print("Error: Debe proporcionar un número válido")
    
    def inorder(self, args):
        print("Recorrido Inorder:", end=" ")
        self.arbol.inorder()
    
    def preorder(self, args):
        print("Recorrido Preorder:", end=" ")
        self.arbol.preorder()
    
    def postorder(self, args):
        print("Recorrido Postorder:", end=" ")
        self.arbol.postorder()
    
    def ayuda(self, args):
        print("\nComandos disponibles:")
        print("agregar <numero> - Agrega un número al árbol")
        print("inorder - Muestra el árbol en recorrido inorder")
        print("preorder - Muestra el árbol en recorrido preorder")
        print("postorder - Muestra el árbol en recorrido postorder")
        print("ayuda - Muestra esta ayuda")
        print("salir - Termina el programa")
    
    def salir(self, args):
        print("¡Hasta luego!")
        return True
    
    def ejecutar(self):
        print("Manejador de Árbol Binario - Escribe 'ayuda' para ver los comandos")
        while True:
            entrada = input("> ").strip().split()
            if not entrada:
                continue
                
            comando = entrada[0].lower()
            args = entrada[1:]
            
            if comando in self.comandos:
                if self.comandos[comando](args):
                    break
            else:
                print("Comando no reconocido. Escribe 'ayuda' para ver los comandos disponibles")

if __name__ == "__main__":
    manejador = ManejadorConsola()
    manejador.ejecutar()