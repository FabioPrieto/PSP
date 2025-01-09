import tkinter as tk

def saludo():
    lblNombre.config(text="Hola: " + txtNombre.get())

ventana = tk.Tk()
ventana.title("Saludo")

#etiqueta label

lblNombre = tk.Label(ventana,text="Dime tu nombre")
lblNombre.pack()

#campo de texto

txtNombre = tk.Entry(ventana)
txtNombre.pack()

#boton

btnSaludo = tk.Button(ventana,text="Saludar", command=saludo)
btnSaludo.pack()

#bucle principal

ventana.geometry("400x200")
ventana.mainloop()