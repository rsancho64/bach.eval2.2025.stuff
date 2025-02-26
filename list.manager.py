#! /usr/bin/python3

class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar(self, descripcion):
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)
        print(f"Tarea '{descripcion}' agregada con éxito.")

    def listar(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
            return
        print("\nLista de tareas:")
        for i, tarea in enumerate(self.tareas, 1):
            estado = "✓" if tarea.completada else "✗"
            print(f"{i}. [{estado}] {tarea.descripcion}")

    def marcar(self, numero):
        try:
            indice = numero - 1
            if 0 <= indice < len(self.tareas):
                self.tareas[indice].completada = True
                print(f"Tarea '{self.tareas[indice].descripcion}' marcada como completada.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    def desmarcar(self, numero):
        try:
            indice = numero - 1
            if 0 <= indice < len(self.tareas):
                self.tareas[indice].completada = False
                print(f"Tarea '{self.tareas[indice].descripcion}' desmarcada.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    def eliminar(self, numero):
        try:
            indice = numero - 1
            if 0 <= indice < len(self.tareas):
                tarea_eliminada = self.tareas.pop(indice)
                print(f"Tarea '{tarea_eliminada.descripcion}' eliminada.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    lista = ListaTareas()
    
    while True:
        print("\n=== Administrador de Tareas ===")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Desmarcar tarea")
        print("5. Eliminar tarea")
        print("6. Salir")
        
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            lista.agregar(descripcion)
            
        elif opcion == "2":
            lista.listar()
            
        elif opcion == "3":
            lista.listar()
            numero = input("Ingrese el número de la tarea a marcar: ")
            lista.marcar(int(numero))
            
        elif opcion == "4":
            lista.listar()
            numero = input("Ingrese el número de la tarea a desmarcar: ")
            lista.desmarcar(int(numero))
            
        elif opcion == "5":
            lista.listar()
            numero = input("Ingrese el número de la tarea a eliminar: ")
            lista.eliminar(int(numero))
            
        elif opcion == "6":
            print("¡Hasta pronto!")
            break
            
        else:
            print("Opción no válida. Por favor, seleccione entre 1 y 6.")

if __name__ == "__main__":
    main()