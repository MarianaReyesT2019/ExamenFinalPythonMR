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
bienvenido.grid(row=0, column=0, columnspan=6)
bienvenido.config(font=('Arial', 20))



#Captura de variables 
nombre = StringVar()
apellido = StringVar()
dia = IntVar()
mes = IntVar()
aneo = IntVar()



#Operacion dias vividos 
def contandoDias():
    fechaString = f"{aneo.get()}-{mes.get()}-{dia.get()}"
    date_object = datetime.strptime(fechaString, '%Y-%m-%d')

    today= datetime.today()
    
    d1 = today
    d2 = date_object
    result1 = abs(d1-d2).days 

    respuesta = f"Nacio --->{date_object} y ha estado viviendo ---> {result1} días."

    lblResul.configure(text = respuesta)

#Operancion nombre al revez 
def contandoLetras():
    sNombre = f"{nombre.get()}"
    sApellido = f"{apellido.get()}"

    conteoN = len(sNombre)
    conteoA = len(sApellido)
  
    if conteoN % 2 == 0:
        n1 = f"{sNombre} Tu nombre es Par "
    else:
        n1 = f"{sNombre} tu nombre es  Inpar"
    if conteoA % 2 == 0:
        a2 = f"{sApellido} tu nombre es  Par."
    else:
        a2 = f"{sApellido} tu nombre es  Inpar."

    respuesta = f"{n1} y  {a2} "

    lblResul.configure(text =respuesta )

def alrevez():
    nene=nombre.get()
    
    reve=nene[::-1]


    lblResul.configure(text =reve)


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
lblaneo=Label(miFrame, text="Año: ")
lblaneo.grid(row=5, column=0)
lblaneo.config(padx=10, pady=10)
txtaneo=Entry(miFrame, textvariable =aneo)
txtaneo.grid(row=5, column=1)


#Botones que se utilizaran para las funciones 
#Bonton 1 funcion 1
btnFuncion1 = Button(miFrame, text="Funcion 1")
btnFuncion1.grid(row=7, column=1)
btnFuncion1.config(padx=6, pady=6)
#Bonton 2 funcion 2
btnFuncion2 = Button(miFrame, text = "Funcion 2", command=contandoDias)
btnFuncion2.grid(row=7, column=2)
btnFuncion2.config(padx=6, pady=6)
#Bonton 3 funcion 
btnFuncion3 = Button(miFrame, text = "Funcion 3", command=contandoLetras)
btnFuncion3.grid(row=7, column=3)
btnFuncion3.config(padx=6, pady=6)
#Bonton 4 funcion 4
btnFuncion4 = Button(miFrame, text = "Funcion 4")
btnFuncion4.grid(row=7, column=4)
btnFuncion4.config(padx=6, pady=6)
#Bonton 5 funcion 5
btnFuncion5 = Button(miFrame, text = "Funcion 5", command=alrevez)
btnFuncion5.grid(row=7, column=5)
btnFuncion5.config(padx=6, pady=6)


#Funcion de Respuestas: Aqui se reacciona 
lblResul=Label(miFrame, text="La respuesta---->")
lblResul.grid(row=9, column=0)
lblResul.config(padx=10, pady=10)
lblR=Label(miFrame)
lblR.grid(row=10, column=0)
lblR.config(padx=10, pady=10)

raiz.mainloop()

