from tkinter import *


global a
global op
a=""
op=""
aux=""
raiz=Tk()
raiz.title("Calculadora Basica")
miframe=Frame(raiz)


raiz.geometry('400x250')
miframe.pack()

numeropantalla=StringVar()
pantalla=Entry(miframe,textvariable=numeropantalla,font=("Roboto Cn",14))
pantalla.grid(row=0 , column=1 , columnspan=8)
pantalla.config(background="black" , fg="#03f943" , justify="right")
numeropantalla.set("0.0")


def numeropulsado(num):
  

    global  a
    if num == "+":
        operaciones(num)
        
    elif num == "-":
        operaciones(num)
            
    elif num=="=":
        operaciones(num)
    elif num=="C":
        numeropantalla.set("0.0")
        
    elif num=="*":
        operaciones(num)
        
    elif num=="/":
        operaciones(num)
        

    else:
        a= a+num
        numeropantalla.set(a)


def operaciones(num):
    
    global a
    global op
    global aux
    
    if num=="+":
        aux=numeropantalla.get()
        op= num
        a=""
    elif num=="-":
        aux=numeropantalla.get()
        op= num
        a=""
    elif num=="C":
        a=""
        op=""
        numeropantalla.set("0")
    elif num=="/":
        aux=numeropantalla.get()
        op= num
        a=""
    elif num=="*":
        aux=numeropantalla.get()
        op= num
        a=""
    else:

        numeropantalla.set(operacion(op,aux))
        a=""
        op=""   
        aux=""  

def operacion(op,aux):
    try:
        
       
        if op=="":
            resultado=numeropantalla.get()

        elif op=="+":
            resultado=float(aux)+float(numeropantalla.get())
        
        elif op=="-":
            resultado=float(aux)-float(numeropantalla.get())
        
        elif op=="/":
            resultado=float(aux)/float(numeropantalla.get())
        
        elif op=="*":
            resultado=float(aux)*float(numeropantalla.get())
    except:
        resultado="ERROR"


    return(resultado)

    
    
botones = ("C",1,4,"7",2,1,"8",2,2,"9",2,3,"/",2,4,"4",3,1,"5",3,2,
"6",3,3,"*",3,4,"1",4,1,"2",4,2,"3",4,3,"-",4,4,"0",5,1,".",5,2,"=",5,3,"+",5,4)
botones_iter = iter(botones)
def botones():
    b=next(botones_iter)   
    e=next(botones_iter)  
    o=next(botones_iter)   
    boton=Button(miframe,text=b,width=8,font=("Roboto Cn",14),command=lambda:numeropulsado(b))
    boton.grid(row=e,column=o)
    return(boton)
boton1=botones()
boton2=botones()
boton3=botones()
boton4=botones()
boton5=botones()
boton6=botones()
boton7=botones()
boton8=botones()
boton9=botones()
boton10=botones()
boton11=botones()
boton12=botones()
boton13=botones()
boton14=botones()
boton15=botones()
boton16=botones()
boton17=botones()


raiz.mainloop()