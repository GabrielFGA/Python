#Acende e apaga um LED através da serial.
import serial
from tkinter import *
from tkinter import ttk
import serial.tools.list_ports


def func_ex():
	#a funcao .encode() tem a finalidade de formatar a msg em utf-8 para ser aceita pela .write
	dt.write(vrb1.get().encode())
	dt.write(vrb2.get().encode())
	dt.write(vrb3.get().encode())		
	print(vrb1.get(),vrb2.get(),vrb3.get())
	print(com_num.get())

#todos=vrb1.get() + vrb2.get() + vrb3.get()

dt=serial.Serial("COM5", 9600)

jan = Tk()
jan.geometry("300x300")
jan.title("LED CONTROL")

vrb1=StringVar()
vrb2=StringVar()
vrb3=StringVar()
com_num=StringVar()

label1=Label(jan, text="LED 1", font=("calibri", 14))
label1.place(x=120, y=5)

rb1l1=Radiobutton(jan, text="Liga", variable=vrb1, value='1')
rb1l1.place(x=80, y=40)

rb2l1=Radiobutton(jan, text="Desliga", variable=vrb1, value='0')
rb2l1.place(x=160, y=40)

label2=Label(jan, text="LED 2", font=("calibri", 14))
label2.place(x=120, y=65)

rb2l1=Radiobutton(jan, text="Liga", variable=vrb2, value='1')
rb2l1.place(x=80, y=90)

rb2l2=Radiobutton(jan, text="Desliga", variable=vrb2, value='0')
rb2l2.place(x=160, y=90)

label3=Label(jan, text="LED 3", font=("calibri", 14))
label3.place(x=120, y=115)

rb3l1=Radiobutton(jan, text="Liga", variable=vrb3, value='1')
rb3l1.place(x=80, y=140)

rb3l2=Radiobutton(jan, text="Desliga", variable=vrb3, value='0')
rb3l2.place(x=160, y=140)

bt1=Button(jan, text="Executa", command=func_ex)
bt1.place(x=120, y=180)

#acha as portas seriais disponíveis e mostra na combobox
portas = list(serial.tools.list_ports.comports())
selbox =ttk.Combobox(jan, textvariable= com_num, values=portas)
selbox.place(x=80, y=220)

jan.mainloop()