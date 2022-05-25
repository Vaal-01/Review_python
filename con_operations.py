
#Ejercicio 12
from gzip import READ


def obrero(horas_laborales):
    horas_laborales=float(horas_laborales)
    if horas_laborales<=40:
           salario_semanal= horas_laborales*10000
    else: 
        horas_extras= horas_laborales-40
        salario_semanal=(40*10000)+(horas_extras*20000)
    return salario_semanal

#Ejercicio 13
def articulo(nom_articulo,precio,clave):
    precio=float(precio)
    if clave==1:
        precio_desc= precio-precio*0.1
        impresion="El articulo "+ nom_articulo +" con un precio \nanterior de " + precio +" tiene un nuevo precio \nde: "+ precio_desc + "usando un \ndescuento del 10%'"    
        return impresion
    elif clave==2: 
        precio_desc= precio-precio*0.2
        impresion="El articulo "+ nom_articulo +" con un precio \nanterior de " + precio +" tiene un nuevo precio \nde: "+ precio_desc + "usando un \ndescuento del 20%'"    
        return impresion
    else:
        impresion="Clave no válida. Solo 1 o 2"
        return impresion

#Ejercicio 14
def icollantas(cant_llantas):
    cant_llantas=int(cant_llantas)
    if cant_llantas<0:
        impresion="Cantidad no válida"
        return impresion
    elif cant_llantas<5:
        total=150000*cant_llantas
        impresion="El total a pagar \nes de: " + total
        return impresion
    else:
        total=138000*cant_llantas
        impresion="El total a pagar \nes de: " + total
        return impresion

#Ejercicio 15
def puls_genero(edad,genero):
    edad=int(edad)
    if genero==2:
        num_pulsaciones=(220-edad)/10
        impresion = "El número de pulsaciones \nque debe tener la \nmujer es de" + num_pulsaciones
        return impresion
    elif  genero==1: 
        num_pulsaciones=(210-edad)/10
        impresion = "El número de pulsaciones \nque debe tener el \nhombre es de" + num_pulsaciones
        return impresion
    else:
        impresion = "Lo sentimos, debes ingresar \nun género válido 1-Masculino \no 2-Femenino"
        return impresion

#Ejercicio 16
def matricula(materias,costo):
    #revisar
    if  materias<=0:
        print( 'Cantidad de materias no válida ')
    elif  materias>5: 
        print( 'Cantidad de materias no válida ')  
    else:
        if materias>=1 :
            nota1=float(input('Ingrese la nota final de la materia 1:  '))
            notas=nota1
        if materias>=2 :
            nota2=float(input('Ingrese la nota final de la materia 2:  '))
            notas=nota1+nota2
        if materias>=3 :
            nota3=float(input('Ingrese la nota final de la materia 3:  '))
            notas=nota1+nota2+nota3
        if materias>=4 :
            nota4=float(input('Ingrese la nota final de la materia 4:  '))
            notas=nota1+nota2+nota3+nota4
        if materias>=5 :
            nota5=float(input('Ingrese la nota final de la materia 5:  '))
            notas=nota1+nota2+nota3+nota4+nota5
        promedio = notas/materias
        if promedio>=4.5:
            matricula=(costo*materias)-((costo*materias)*0.30)
            print('El valor de matrícula con descuento del 30% que debe pagar el aprendiz es de:  ', matricula)
        elif promedio<4.5:
            if promedio>0:
                matricula=(costo*materias)+(costo*materias)*0.10
                print('El valor de matrícula más iva que debe pagar el aprendiz es de:  ', matricula)

#Ejercicio 17
def azar(total_compra,num_azar):
    num_azar=int(num_azar)
    total_compra=float(total_compra)
    if num_azar<0:
        return ("Lo sentimos, debes \ningresar un número mayor \n a cero")
    elif  num_azar<74:
        descuento=0.15*total_compra
        return ("El descuento usado es del \n15% por lo que se le\n descontó " + descuento + " de \nla compra")
    else:
        descuento=0.20*total_compra
        return ("El descuento usado es del \n20% por lo que se le\n descontó " + descuento + " de \nla compra")

#Ejercicio 18
def romano(num_entero):
    num_entero=int(num_entero)
    if num_entero==1:
        return num_entero,"I"
    elif  num_entero==2:
        return num_entero,"II"
    elif  num_entero==3:
        return num_entero,"III"
    elif  num_entero==4:
        return num_entero,"IV"
    elif  num_entero==5:
        return num_entero,"V"
    elif  num_entero==6:
        return num_entero,"VI"
    elif  num_entero==7:
        return num_entero,"VII"
    elif  num_entero==8:
        return num_entero,"VIII"
    elif  num_entero==9:
        return num_entero,"IX"
    elif  num_entero==10:
        return num_entero,"X"
    else:
        return num_entero,"inválido"
        
#Ejercicio 19

#Ejercicio 20
#Ejercicio 21
#Ejercicio 22
