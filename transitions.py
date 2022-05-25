import seq_operations 

#Global Variables
temp=0
enunciado=""
entrada=""
salida1=""

def asignar(num):
    global temp
    temp=num

def get_enunciado():
    global enunciado,entrada
    if get_temp()==2:
        enunciado="Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente \n desea saber cuánto deberá pagar finalmente por su compra."
        entrada="Valor Compra"
    return enunciado

def process1(valor):
    global salida1
    if get_temp()==2:
        salida1="El valor final \n de la compra con \ndescuento de 15% es \n de "+ str(seq_operations.compra(valor))

def get_entrada():
    return entrada
     
def get_temp():
    return temp

def get_salida1():
    return salida1