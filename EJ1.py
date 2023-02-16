import tkinter as tk
from tkinter import *

ventana = Tk()

ventana.title('Indice de Masa Corporal')
ventana.geometry('300x215')
ventana.resizable(0,0)
ventana.config(bg="#ECADA0")

def calcular():
    pe = float(peso.get())
    altu = float(altura.get())

    imcc = pe/(altu*altu)

    resultado.set(round(imcc,2))

    if (imcc<18.5):
        cc.set("Peso inferior al normal")
    elif (imcc>=18.5 and imcc<=24.9):
        cc.set("Normal")
    elif (imcc>=25 and imcc<=29.9):
        cc.set("Peso superior al normal")
    else:
        cc.set("Obesidad")


Label(ventana, text='CALCULAR IMC',bg="#ECADA0").place(x=95,y=5)

Label(ventana, text='Ingrese peso:',bg="#ECADA0").place(x=10,y=30)
peso = Entry(ventana, width=25, bd=5)
peso.place(x=110,y=30)

Label(ventana, text='Ingrese altura (m):',bg="#ECADA0").place(x=10,y=60)
altura = Entry(ventana, width=25, bd=5)
altura.place(x=110,y=60)

Button(ventana, text='Calcular', command=calcular,bg="#B0B3B4").place(x=115,y=100)

resultado=tk.StringVar()
imc = Entry(ventana, width= 25,bd= 5, justify = 'right', state = tk.DISABLED,textvariable= resultado).place(x=75,y=140)
cc=tk.StringVar()
composicion = Entry(ventana, width= 25,bd= 5, justify = 'right', state = tk.DISABLED,textvariable= cc).place(x=75,y=170)

ventana.mainloop()
