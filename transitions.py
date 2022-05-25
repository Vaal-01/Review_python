import seq_operations 

#Global Variables
temp=0
enunciado=""
entrada=""
salida1=""
entrada1=""
entrada2=""
entrada3=""


def asignar(num):
    global temp
    temp=num

def get_entrada():
    return entrada

def get_entrada1():
    return entrada1
    
def get_entrada2():
    return entrada2
    
def get_entrada3():
    return entrada3
    
def get_temp():
    return temp

def get_salida1():
    return salida1

#Return data    
def get_enunciado():
    global enunciado,entrada,salida1,entrada1,entrada2,entrada3
    salida1=""
    if get_temp()==2:
        enunciado="Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente \n desea saber cuánto deberá pagar finalmente por su compra."
        entrada="Valor Compra"
    if get_temp()==4:
        enunciado="Programa para calcular el porcentaje de mujeres y hombres que hay dentro\n de un grupo de estudiantes"
        entrada1="Cantidad Mujeres"
        entrada2="Cantidad Hombres"
    if get_temp()==6:
        enunciado="Programa para calcular la equivalencia de pesos colombianos a dólares"
        entrada1="Pesos"
        entrada2="Valor Dolar"
    if get_temp()==7:
        enunciado="Programa para calcular el número de pulsaciones que una persona debe  \ntener por cada 10 segundos de ejercicio según su edad."
        entrada="Edad"
    if get_temp()==8:
        enunciado="Programa para calcular el nuevo salario de un obrero si obtuvo un incremento \ndel 25% sobre su salario anterior"
        entrada="Salario anterior"
    if get_temp()==9:
        enunciado="Programa para calcular el precio en que se debe vender el producto determinado \npara obtener una ganancia del 30%"
        entrada="Precio Artículo"
    if get_temp()==10:
        enunciado="Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas \ninvierte una cantidad distinta. Este programa obtiene el porcentaje que \ncada quien invierte con respecto a la cantidad total invertida"
        entrada1="Inversión 1"
        entrada2="Inversión 2"
        entrada3="Inversión 3"
    if get_temp()==11:
        enunciado="Programa para calcular la masa de aire segun la presión, volumen y temperatura"
        entrada1="Presión"
        entrada2="Volumen"
        entrada3="Temperatura"
    return enunciado

def process1(valor):
    global salida1
    salida1=""
    if get_temp()==2:
        salida1="El valor final \n de la compra con \ndescuento de 15% es \n de "+ str(seq_operations.compra(valor))
    if get_temp()==7:
        salida1="Las pulsaciones que \n debe tener por  \ncada 10 segundos de  \nejercicio son " + str(seq_operations.pulsaciones(valor))
    if get_temp()==8:
        salida1="El nuevo salario\n del obrero con el \nincremento del 25% es \nde "+ str(seq_operations.obrero(valor))
    if get_temp()==9:
        salida1="El valor por el \nque debe venderse el\n producto para obtener \nuna ganancia del \n30% es de "+ str(seq_operations.ganancia(valor))

def process2(valor1,valor2):
    global salida1
    salida1=""
    if get_temp()==4:
        salida1="Dentro del grupo de estudiantes,\n el porcentaje de mujeres es de:\n " + str(seq_operations.porcentajes(valor1,valor2)[0]) + "% por lo que el\n de hombres será: " +str(seq_operations.porcentajes(valor1,valor2)[1]) +"%"
    if get_temp()==6:
        salida1="La equivalencia de pesos \ncolombianos a dólares es de: \n" + str(seq_operations.equivalencia(valor1,valor2))

def process3(valor1,valor2,valor3):
    global salida1
    salida1=""
    if get_temp()==10:
        salida1="El porcentaje de inversión del \n1 socio es de: "+ str(seq_operations.inversion(valor1,valor2,valor3)[0]) +"%, del 2 socio \nde: "+ str(seq_operations.inversion(valor1,valor2,valor3)[1]) +"% y del 3 socio \nde: " + str(seq_operations.inversion(valor1,valor2,valor3)[2]) + "%"
    if get_temp()==11: 
        salida1="La masa del aire es\n de: "+ str(seq_operations.masa(valor1,valor2,valor3))