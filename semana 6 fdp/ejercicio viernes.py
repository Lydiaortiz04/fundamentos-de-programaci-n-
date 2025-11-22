import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Prueba de Tkinter")
ventana.geometry("300x200")

#Etiqueta
etiqueta = tk.Label(ventana, text= "✓ Tkinter funciona correctamente", font=("Arial", 12))


#Boton
def mostar_mensaje():
    messagebox.showinfo("Exito", "¡La libreria tkinter esta funcionando!")
boton= tk.Button(ventana, text="Hacer clic aqui", command=mostar_mensaje)
boton.pack(pady=10)
#Iniciar la aplicación
ventana.mainloop()