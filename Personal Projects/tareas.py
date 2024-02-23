import tkinter as tk

def agregar_tarea():
    tarea = entrada_tarea.get()
    # Agregar lógica para agregar la tarea a la lista
    print("Tarea agregada:", tarea)
    entrada_tarea.delete(0, tk.END)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Crear un cuadro de texto para ingresar la tarea
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=10)

# Crear un botón para agregar la tarea
boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack()

# Ejecutar el bucle de eventos
ventana.mainloop()
