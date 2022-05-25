
#Ejercicio 1
import re


def vendedor(sueldo,venta1,venta2,venta3):
    salario= sueldo+(venta1+venta2+venta3)*0.1
    return salario

#Ejercicio 2
def compra(valor_compra):
    valor_final= valor_compra - (valor_compra *0.15)
    return valor_final

#Ejercicio 3
def aprendiz(parcial1,parcial2,parcial3,examen,trabajo):
    nota_final=((parcial1+parcial2+parcial3)/3)*0.55+(examen*0.3)+(trabajo*0.15)
    return nota_final

#Ejercicio 4
def porcentajes(cant_mujeres,cant_hombres):
    total=cant_mujeres+cant_hombres
    porcentaje_mujeres= (cant_mujeres/total)*100
    porcentaje_hombres= (cant_hombres/total)*100
    return porcentaje_mujeres,porcentaje_hombres

#Ejercicio 5
def edad(ano_nacimiento,mes_nacimiento,dia_nacimiento,ano_actual,mes_actual,dia_actual):
    edad = ano_actual - ano_nacimiento
    if mes_nacimiento>mes_actual:
        edad=edad-1
    elif  mes_nacimiento==mes_actual :
        if dia_nacimiento>dia_actual:
            edad=edad-1
    return edad

#Ejercicio 6
def equivalencia(cpesos,ucambiaria):
    equivalencia=cpesos/ucambiaria
    return equivalencia

#Ejercicio 7
def pulsaciones(edad):
    num_pulsaciones=(220-edad)/10
    return num_pulsaciones

#Ejercicio 8
def obrero(salario_anterior):
    nuevo_salario= salario_anterior + (salario_anterior*0.25)
    return nuevo_salario

#Ejercicio 9
def ganancia(precio):
    venta=precio + (precio*0.30)
    return venta

#Ejercicio 10
def inversion(inversion1,inversion2,inversion3):
    total=inversion1+inversion2+inversion3
    porcentaje1=(inversion1/total)*100
    porcentaje2=(inversion2/total)*100
    porcentaje3=(inversion3/total)*100
    #Revisar return

#Ejercicio 11
def masa(presion,volumen,temperatura):
    masa=(presion*volumen)/(0.37*(temperatura+460))
    return masa


