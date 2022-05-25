
#Ejercicio 1
def vendedor(sueldo,venta1,venta2,venta3):
    sueldo = float(sueldo)
    venta1 = float(venta1)
    venta2 = float(venta2)
    venta3 = float(venta3)
    salario= sueldo+(venta1+venta2+venta3)*0.1
    return salario

#Ejercicio 2
def compra(valor_compra):
    valor_compra = float(valor_compra)
    valor_final= valor_compra - (valor_compra *0.15)
    return valor_final

#Ejercicio 3
def aprendiz(parcial1,parcial2,parcial3,examen,trabajo):
    parcial1 = float(parcial1)
    parcial2 = float(parcial2)
    parcial3 = float(parcial3)
    examen = float(examen)
    trabajo = float(trabajo)
    nota_final=round((((parcial1+parcial2+parcial3)/3)*0.55+(examen*0.3)+(trabajo*0.15)),4)
    return nota_final

#Ejercicio 4
def porcentajes(cant_mujeres,cant_hombres):
    cant_mujeres = float(cant_mujeres)
    cant_hombres = float(cant_hombres)
    total=cant_mujeres+cant_hombres
    porcentaje_mujeres= round(((cant_mujeres/total)*100),2)
    porcentaje_hombres= round(((cant_hombres/total)*100),2)
    return porcentaje_mujeres,porcentaje_hombres

#Ejercicio 5
def edad(ano_nacimiento,mes_nacimiento,dia_nacimiento,ano_actual,mes_actual,dia_actual):
    ano_nacimiento = float(ano_nacimiento)
    mes_nacimiento = float(mes_nacimiento)
    dia_nacimiento = float(dia_nacimiento)
    ano_actual = float(ano_actual)
    mes_actual = float(mes_actual)
    dia_actual = float(dia_actual)

    edad = ano_actual - ano_nacimiento
    if mes_nacimiento>mes_actual:
        edad=edad-1
    elif  mes_nacimiento==mes_actual :
        if dia_nacimiento>dia_actual:
            edad=edad-1
    return edad

#Ejercicio 6
def equivalencia(cpesos,ucambiaria):
    cpesos = float(cpesos)
    ucambiaria = float(ucambiaria)
    equivalencia=cpesos/ucambiaria
    return equivalencia

#Ejercicio 7
def pulsaciones(edad):
    edad = float(edad)
    num_pulsaciones=(220-edad)/10
    return num_pulsaciones

#Ejercicio 8
def obrero(salario_anterior):
    salario_anterior = float(salario_anterior)
    nuevo_salario= salario_anterior + (salario_anterior*0.25)
    return nuevo_salario

#Ejercicio 9
def ganancia(precio):
    precio=float(precio)
    venta=precio + (precio*0.30)
    return venta

#Ejercicio 10
def inversion(inversion1,inversion2,inversion3):
    inversion1 = float(inversion1)
    inversion2 = float(inversion2)
    inversion3 = float(inversion3)
    total=inversion1+inversion2+inversion3
    porcentaje1=round(((inversion1/total)*100),2)
    porcentaje2=round(((inversion2/total)*100),2)
    porcentaje3=round(((inversion3/total)*100),2)
    return porcentaje1,porcentaje2,porcentaje3

#Ejercicio 11
def masa(presion,volumen,temperatura):
    presion = float(presion)
    volumen = float(volumen)
    temperatura = float(temperatura)
    masa=(presion*volumen)/(0.37*(temperatura+460))
    return masa


