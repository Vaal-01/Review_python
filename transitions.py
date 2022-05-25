import seq_operations 

#Global Variables
temp=0
enunciado=""
entrada=""
salida1=""

def asignar(num):
    global temp
    temp=num

def get_entrada():
    return entrada
     
def get_temp():
    return temp

def get_salida1():
    return salida1

#Return data    
def get_enunciado():
    global enunciado,entrada,salida1
    salida1=""
    if get_temp()==2:
        enunciado="Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente \n desea saber cuánto deberá pagar finalmente por su compra."
        entrada="Valor Compra"
    if get_temp()==7:
        enunciado="Programa para calcular el número de pulsaciones que una persona debe  \ntener por cada 10 segundos de ejercicio según su edad."
        entrada="Edad"
    if get_temp()==8:
        enunciado="Programa para calcular el nuevo salario de un obrero si obtuvo un incremento \ndel 25% sobre su salario anterior"
        entrada="Salario anterior"
    if get_temp()==9:
        enunciado="Programa para calcular el precio en que se debe vender el producto determinado \npara obtener una ganancia del 30%"
        entrada="Precio Artículo"
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


