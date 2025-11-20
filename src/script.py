import tkinter as tk
from tkinter import messagebox

def mostrarMensaje():
    messagebox.showinfo("Aviso", "Botón presionado!")

ventana = tk.Tk()
ventana.title("Mi primera ventana")

label = tk.Label(ventana, text="Presiona el botón para ver un mensaje")
label.pack(pady=10)

boton = tk.Button(ventana, text="Haz click aca", command=mostrarMensaje)
boton.pack(pady=10)

ventana.mainloop()