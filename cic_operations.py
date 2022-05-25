from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import time

#Global Variables
peso_nino=0
cant_nino=0
peso_ado=0
cant_ado=0
peso_jov=0
cant_jov=0
peso_adul=0
cant_adul=0
peso_viejo=0
cant_viejo=0
prom_nino=0
prom_ado=0
prom_jov=0
prom_adul=0
prom_viejo=0
ganancia=0

#Ejercicio 1
def positivo():
    impresion="Listado de números\n"
    for i in range(10):
        num=simpledialog.askinteger(title="Ejercicio1",prompt="Escriba el número "+str(i+1))
        num=int(num)
        if num>0:
            impresion+="El número "+ str(num) +" SI es positivo\n"
    return impresion

#Ejercicio 2
def conversion():
    impresion="Listado de números\n"
    for i in range(15):
        num=simpledialog.askinteger(title="Ejercicio2",prompt="Escriba el número "+str(i+1))
        num=int(num)
        if num<0:
            impresion+="El número "+ str(num) +" convertido a positivo es " + str(abs(num)) +"\n"
    return impresion

#Ejercicio 3
def reloj():
    impresion="Reloj Digital\n"
    for h in range(1):
        for m in range(1):
            for s in range(10):
                impresion+=str(h)+":"+str(m)+":"+str(s)+"\n"
                time.sleep(1)
    return impresion

#Ejercicio 4
def promedio():
    global peso_nino,cant_nino,peso_ado,cant_ado,peso_jov,cant_jov,peso_adul,cant_adul,peso_viejo,cant_viejo,prom_nino,prom_ado,prom_jov,prom_adul,prom_viejo

    impresion="Resultados\n"
    for i in range(5):
        edad=simpledialog.askinteger(title="Ejercicio4",prompt="Ingrese la edad de la persona "+str(i+1))
        edad=int(edad)
        peso=simpledialog.askinteger(title="Ejercicio4",prompt="Ingrese el peso de la persona "+str(i+1))
        peso=float(peso)
        if edad<0:
            impresion="Edad de la persona "+str(i+1) +" inválida \n"
        elif edad<=12:
            peso_nino=peso_nino+peso
            cant_nino=cant_nino+1
            prom_nino=peso_nino/cant_nino
        elif edad<=17:
            peso_ado=peso_ado+peso
            cant_ado=cant_ado+1
            prom_ado=peso_ado/cant_ado
        elif edad<=29:
            peso_jov=peso_jov+peso
            cant_jov=cant_jov+1
            prom_jov=peso_jov/cant_jov
        elif edad<=59:
            peso_adul=peso_adul+peso
            cant_adul=cant_adul+1
            prom_adul=peso_adul/cant_adul
        else:
            peso_viejo=peso_viejo+peso
            cant_viejo=cant_viejo+1
            prom_viejo=peso_viejo/cant_viejo

    impresion+="Promedio de peso de niños: "+str(prom_nino)+"\n"
    impresion+="Promedio de peso de adolescentes: "+str(prom_ado)+"\n"
    impresion+="Promedio de peso de jóvenes: "+str(prom_jov)+"\n"
    impresion+="Promedio de peso de adultos: "+str(prom_adul)+"\n"
    impresion+="Promedio de peso de viejos: "+str(prom_viejo)+"\n"
    return impresion

#Ejercicio 5
def ganancias():
    global ganancia
    impresion="Resultados\n"
    precio=simpledialog.askinteger(title="Ejercicio5",prompt="Ingrese el precio del kilo de naranjas")
    precio=float(precio)
    for i in range(10):
        kilos=simpledialog.askinteger(title="Ejercicio5",prompt="Ingrese  la cantidad de kilos de naranjas a comprar de la persona "+str(i+1))
        kilos=int(kilos)
        if kilos<0:
            impresion+="Cantidad inválida para la persona "+str(i+1) +"\n"  
        elif kilos>10:
            total=(precio*kilos)-((precio*kilos)*0.15)
            impresion+="Se aplicó un descuento de 15% para la persona "+str(i+1) +" y debe pagar: " +str(total) +"\n"
        else:
            total=precio*kilos
            impresion+="La persona "+str(i+1) +" debe pagar: " +str(total) +"\n" 
        ganancia=ganancia+total
    impresion+="La ganancia obtenida de la tienda fue COP " +str(ganancia)
    return impresion

#Ejercicio 6
def tablas():
    for i in range(10):
        impresion=""
        impresion+="TABLA DE MULTIPLICAR DEL "+str(i+1)+"\n"
        for j in range(10):
            impresion+=str(i+1) +"x"+ str(j+1) +"=" + str((i+1)*(j+1))+"\n"
        messagebox.showinfo("Tabla de multiplicar",impresion)

#Ejercicio 7
def primo(num):
    num=int(num)
    temp=0
    for i in range(num):
        if num % (i+1) == 0:
            temp = temp + 1
    if temp == 2: 
        return("El numero "+ str(num) +" es primo")
    else:
        return("El numero "+ str(num) +" no \nes primo")

#Ejercicio 8
def multiplicar(num):
    num=int(num)
    impresion= "TABLA DE MULTIPLICAR DEL "+str(num) +"\n"
    for i in range(10):
        impresion+=(str(num)+"x"+str(i)+"="+str(num*i)+"\n")
    return impresion