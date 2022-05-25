
#Ejercicio 12
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
    clave=int(clave)
    if clave==1:
        precio_desc= precio-precio*0.1
        impresion="El articulo "+ str(nom_articulo) +" con un \nprecio anterior de " + str(precio) +" tiene \nun nuevo precio de: "+ str(precio_desc) + " \nusando un descuento del 10%"    
        return impresion
    elif clave==2: 
        precio_desc= precio-precio*0.2
        impresion="El articulo "+ str(nom_articulo) +" con un \nprecio anterior de " + str(precio) +" tiene \nun nuevo precio de: "+ str(precio_desc) + " \nusando un descuento del 20%"    
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
        impresion="El total a pagar es de: \n" + str(total)
        return impresion
    else:
        total=138000*cant_llantas
        impresion="El total a pagar es de: \n" + str(total)
        return impresion

#Ejercicio 15
def puls_genero(edad,genero):
    edad=int(edad)
    genero=int(genero)
    if genero==2:
        num_pulsaciones=(220-edad)/10
        impresion = "El número de pulsaciones que \ndebe tener la mujer es de\n" + str(num_pulsaciones)
        return impresion
    elif  genero==1: 
        num_pulsaciones=(210-edad)/10
        impresion = "El número de pulsaciones que \ndebe tener el hombre es de\n" + str(num_pulsaciones)
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
        return ("El descuento usado es del 15%\n por lo que se le descontó \n" + str(descuento) + " de la compra")
    else:
        descuento=0.20*total_compra
        return ("El descuento usado es del 20%\n por lo que se ledescontó\n " + str(descuento) + " de la compra")

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
def descuento(total_venta,codigo):
    codigo=int(codigo)
    total_venta=float(total_venta)
    if codigo==1:
        valor_venta=total_venta-total_venta*0.02
        return ("Se realizó un descuento del 2%\n dando como total un valor \nde: "+str(valor_venta))
    elif  codigo==2:
        valor_venta=total_venta-total_venta*0.03
        return ("Se realizó un descuento del 3%\n dando como total un valor \nde: "+str(valor_venta))
    elif  codigo==5:
        valor_venta=total_venta-total_venta*0.05
        return ("Se realizó un descuento del 5%\n dando como total un valor \nde: "+str(valor_venta))
    elif  codigo==7:
        valor_venta=total_venta-total_venta*0.08
        return ("Se realizó un descuento del 8%\n dando como total un valor \nde: "+str(valor_venta))
    elif  codigo==10:
        valor_venta=total_venta-total_venta*0.1
        return ("Se realizó un descuento del 10%\n dando como total un valor \nde: "+str(valor_venta))
    elif  codigo==11:
        valor_venta=total_venta-total_venta*0.15
        return ("Se realizó un descuento del 15%\n dando como total un valor \nde:"+str(valor_venta))
    else:
        return "Código no válido"

#Ejercicio 20
def balota(balota,precio_compra):
    balota=int(balota)
    precio_compra=float(precio_compra)
    if balota==1:
        return("Premio Obtenido: Bolsa de Leche \n Valor Compra: "+ str(precio_compra))
    elif  balota==2:
        return("Premio Obtenido: Libra de Arroz \n Valor Compra: "+ str(precio_compra))
    elif  balota==3:
        return("Premio Obtenido: 1 Dulce \n Valor Compra: "+ str(precio_compra))
    elif  balota==4:
        return("Premio Obtenido: 1 Menta \n Valor Compra: "+ str(precio_compra))
    elif  balota==5:
        return("Vuelve a intentar\n Valor Compra: "+ str(precio_compra))
    elif  balota==6:
        return("Premio Obtenido: 1 Papas Fritas \n Valor Compra: "+ str(precio_compra))
    elif  balota==7:
        valor_apagar=precio_compra-(precio_compra*0.1)
        return("Descuento Obtenido: 10% \n Valor Compra: "+ str(valor_apagar))
    elif  balota==8:
        valor_apagar=precio_compra-(precio_compra*0.12)
        return("Descuento Obtenido: 12% \n Valor Compra: "+ str(valor_apagar))
    elif  balota==9:
        return("No hay premio\n Valor Compra: "+ str(precio_compra))
    elif  balota==10:
        valor_apagar=precio_compra-(precio_compra*0.15)
        return("Descuento Obtenido: 15% \n Valor Compra: "+ str(valor_apagar))
    else:
        return "Número de balota inválido"

#Ejercicio 21
def operaciones(num1,num2,opcionn):
    num1=int(num1)
    num2=int(num2)
    opcionn=float(opcionn)
    if  opcionn==1:
        suma=num1+num2
        return ("El resultado de la Suma es: "+str(suma))
    elif  opcionn==2:
        resta=num1-num2
        return ("El resultado de la Resta es: "+str(resta))
    elif  opcionn==3:
        multiplicacion=num1*num2
        return ("El resultado de la Multiplicación \nes: "+str(multiplicacion))
    elif  opcionn==4:
        if num2==0:
            return "No es posible dividir entre cero"
        else:
            division=num1/num2
            return ("El resultado de la División es: \n"+str(division))
    else:
        return "Número de opción inválido"

#Ejercicio 22
def nota(grado,evaluacion,trabajos,comportamiento):
    grado=int(grado)
    evaluacion=float(evaluacion)
    trabajos=float(trabajos)
    comportamiento=float(comportamiento)
    if grado>11:
        return "Número de opción inválido"
    else: 
        if  grado==1:
            nota=(evaluacion*0.15)+(trabajos*0.15)+(comportamiento*0.70)
        elif  grado==2:
            nota=(evaluacion*0.20)+(trabajos*0.40)+(comportamiento*0.40)
        elif  grado==3:
            nota=(evaluacion*0.10)+(trabajos*0.70)+(comportamiento*0.20)
        elif  grado==4:
            nota=(evaluacion*0.45)+(trabajos*0.05)+(comportamiento*0.40)
        elif  grado==5:
            nota=(evaluacion*0.40)+(trabajos*0.10)+(comportamiento*0.50)
        elif  grado==6:
            nota=(evaluacion*0.30)+(trabajos*0.40)+(comportamiento*0.30)
        elif grado==7:
            nota=(evaluacion*0.40)+(trabajos*0.40)+(comportamiento*0.20)
        elif  grado==8:
            nota=(evaluacion*0.30)+(trabajos*0.50)+(comportamiento*0.20)
        elif  grado==9:
            nota=(evaluacion*0.70)+(trabajos*0.30)
        elif  grado==10:
            nota=(evaluacion*0.60)+(trabajos*0.30)+(comportamiento*0.10)
        elif  grado==11:
            nota=(evaluacion*0.50)+(trabajos*0.40)+(comportamiento*0.10)
    return ("La nota final del estudiante \nes de: " + str(nota)) 