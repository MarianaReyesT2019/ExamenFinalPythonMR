from tkinter import *
from datetime import date
from datetime import datetime


#Inicio
raiz = Tk()
raiz.geometry("500x500")
raiz.title("Examen Final Python Mariana Reyes")
miFrame= Frame()
miFrame.pack()
bienvenido = Label(miFrame, text="...Bienvenidos...")
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('Arial', 16))



#--Capturando variables
nombre = StringVar()
apellido = StringVar()
dia = IntVar()
mes = IntVar()
anio = IntVar()

#Creando inputs nombre, apellido, dia, mes, año 
#input nombre 
lblnombre= Label(miFrame, text="Nombre: ")
lblnombre.grid(row=1, column=0)
lblnombre.config(padx=10, pady=10)
txtNombre=Entry(miFrame, textvariable =nombre)
txtNombre.grid(row=1, column=1)

#Input apellido
lblapellido=Label(miFrame, text="Apellido: ")
lblapellido.grid(row=2, column=0)
lblapellido.config(padx=10, pady=10)
txtApellido=Entry(miFrame, textvariable =apellido)
txtApellido.grid(row=2, column=1)

#Input dia 
lbldia=Label(miFrame, text="Día: ")
lbldia.grid(row=3, column=0)
lbldia.config(padx=10, pady=10)
txtDia=Entry(miFrame, textvariable =dia)
txtDia.grid(row=3, column=1)

#Input mes 
lblmes=Label(miFrame, text="Mes: ")
lblmes.grid(row=4, column=0)
lblmes.config(padx=10, pady=10)
txtMes=Entry(miFrame, textvariable =mes)
txtMes.grid(row=4, column=1)

#Input año 
lblanio=Label(miFrame, text="Año: ")
lblanio.grid(row=5, column=0)
lblanio.config(padx=10, pady=10)
txtanio=Entry(miFrame, textvariable =anio)
txtanio.grid(row=5, column=1)