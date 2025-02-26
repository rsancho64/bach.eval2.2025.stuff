import tkinter as tk
from tkinter import messagebox

class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Tareas")
        self.root.geometry("400x500")
        
        self.tareas = []
        
        # Frame para entrada
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(pady=10)
        
        self.entry = tk.Entry(self.entry_frame, width=30)
        self.entry.pack(side=tk.LEFT, padx=5)
        
        self.add_button = tk.Button(self.entry_frame, text="Agregar", command=self.agregar_tarea)
        self.add_button.pack(side=tk.LEFT)
        
        # Frame para lista
        self.list_frame = tk.Frame(root)
        self.list_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox = tk.Listbox(self.list_frame, height=15, width=40,
                                     yscrollcommand=self.scrollbar.set)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        # Frame para botones
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        
        self.mark_button = tk.Button(self.button_frame, text="Marcar", 
                                   command=self.marcar_tarea)
        self.mark_button.pack(side=tk.LEFT, padx=5)
        
        self.unmark_button = tk.Button(self.button_frame, text="Desmarcar", 
                                     command=self.desmarcar_tarea)
        self.unmark_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_button = tk.Button(self.button_frame, text="Eliminar", 
                                     command=self.eliminar_tarea)
        self.delete_button.pack(side=tk.LEFT, padx=5)
        
        # Vincular Enter a agregar tarea
        self.root.bind('<Return>', lambda event: self.agregar_tarea())

    def actualizar_lista(self):
        self.task_listbox.delete(0, tk.END)
        for tarea in self.tareas:
            estado = "✓" if tarea.completada else "✗"
            self.task_listbox.insert(tk.END, f"[{estado}] {tarea.descripcion}")

    def agregar_tarea(self):
        descripcion = self.entry.get().strip()
        if descripcion:
            nueva_tarea = Tarea(descripcion)
            self.tareas.append(nueva_tarea)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una descripción.")

    def marcar_tarea(self):
        try:
            indice = self.task_listbox.curselection()[0]
            self.tareas[indice].completada = True
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea primero.")

    def desmarcar_tarea(self):
        try:
            indice = self.task_listbox.curselection()[0]
            self.tareas[indice].completada = False
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea primero.")

    def eliminar_tarea(self):
        try:
            indice = self.task_listbox.curselection()[0]
            del self.tareas[indice]
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea primero.")

def main():
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()

if __name__ == "__main__":
    print("go")
    main()
    
