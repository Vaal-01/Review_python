import seq_operations, con_operations

#Global Variables
temp=0
enunciado=""
entrada=""
salida1=""
entrada1=""
entrada2=""
entrada3=""
entrada4=""
entrada5=""
entrada6=""

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

def get_entrada4():
    return entrada4

def get_entrada5():
    return entrada5

def get_entrada6():
    return entrada6
    
def get_temp():
    return temp

def get_salida1():
    return salida1

#Return data    
def get_enunciado():
    global enunciado,entrada,salida1,entrada1,entrada2,entrada3,entrada4,entrada5,entrada6
    salida1=""
    if get_temp()==1:
        enunciado="Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el \nvendedor desea saber cuánto dinero obtendrá por concepto\n de comisiones por las tres ventas que realiza en el mes y el \ntotal que recibirá en el mes tomando en cuenta su sueldo base y comisiones"
        entrada1="Sueldo Base"
        entrada2="Primera venta"
        entrada3="Segunda venta"
        entrada4="Tercera venta"
    if get_temp()==2:
        enunciado="Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente \n desea saber cuánto deberá pagar finalmente por su compra."
        entrada="Valor Compra"
    if get_temp()==3:
        enunciado="Un aprendiz desea saber cuál será su calificación final en la materia de Algoritmos. Dicha \n calificación se compone de los siguientes porcentajes: \n 55% del promedio de sus tres calificaciones parciales, 30% de la calificación \n del examen final y 15% de la calificación de un trabajo final"
        entrada1="Parcial 1"
        entrada2="Parcial 2"
        entrada3="Parcial 3"
        entrada4="Examen Final"
        entrada5="Trabajo Final"
    if get_temp()==4:
        enunciado="Programa para calcular el porcentaje de mujeres y hombres que hay dentro\n de un grupo de estudiantes"
        entrada1="Cantidad Mujeres"
        entrada2="Cantidad Hombres"
    if get_temp()==5:
        enunciado="Programa para calcular la edad de una persona"
        entrada1="Año Nacimiento"
        entrada2="Mes Nacimiento"
        entrada3="Día Nacimiento"
        entrada4="Año Actual"
        entrada5="Mes Actual"
        entrada6="Día Actual"
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
    if get_temp()==12:
        enunciado="Un obrero necesita calcular su salario semanal, el cual se obtiene de la \nsiguiente manera:Si trabaja 40 horas o menos se le paga 10.000 por hora. \n Si trabaja más de 40 horas se le paga 10.000 por cada una de las primeras \n40 horas y 20.000 por cada hora extra."
        entrada="Horas Trabajadas"
    if get_temp()==13:
        enunciado="Programa que imprime el nombre de un artículo, clave, precio original y su precio\n con descuento. El descuento lo hace en base a la clave, si la clave es 01 el descuento \nes del 10% y si la clave es 02 el descuento es del 20% (solo existen dos claves)."
        entrada1="Nombre Articulo"
        entrada2="Precio Articulo"
        entrada3="Clave"
    if get_temp()==14:
        enunciado="La empresa Icollantas desea un sistema de información para calcular el total \nque una persona debe pagar en un punto de venta, si el precio de \ncada llanta es de 150.000 si se compran menos de 5 llantas y de 138.000 \nsi se compran 5 o más."
        entrada="Cantidad LLantas"
    if get_temp()==15:
        enunciado="Programa para calcular el número de pulsaciones que debe tener una persona por \ncada 10 segundos de ejercicio aeróbico según su edad \ny género (1-Masculino o 2-Femenino)."
        entrada1="Edad"
        entrada2="Género"
    if get_temp()==17:
        enunciado="En un supermercado se hace una promoción, mediante la cual el cliente obtiene \nun descuento dependiendo de un número que se escoge al azar."
        entrada1="Valor Compra"
        entrada2="Número azar"
    if get_temp()==18:
        enunciado="Programa para obtener el equivalente de ingresar un número entero (1 a 10) \na romano"
        entrada="Número entero"
    if get_temp()==19:
        enunciado="Programa que permite ingresar el total de una venta y el código del cajero de lo\n atendió, y así obtener un descuento"
        entrada1="Total Venta"
        entrada2="Código Cajero"
    if get_temp()==20:
        enunciado="El hipermercado del barrio ha implementado un sistema de rifas para sus clientes \npor medio de balotas marcadas con los números y premios"
        entrada1="Balota"
        entrada2="Valor Compra"
    if get_temp()==21:
        enunciado="Programa para realizar operaciones entre dos números según una opción así:\n (1-Suma , 2-Resta, 3-Multiplicación, 4-División) "
        entrada1="Número 1"
        entrada2="Número 2"
        entrada3="Opción"
    if get_temp()==22:
        enunciado="Programa para calcular la nota de los estudiantes de grado primero a once"
        entrada1="Grado"
        entrada2="Evaluación"
        entrada3="Trabajos"
        entrada4="Comportamiento"
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
    if get_temp()==12:
        salida1="El salario semanal fue \nde:" + str(con_operations.obrero(valor))
    if get_temp()==14:
        salida1=str(con_operations.icollantas(valor))
    if get_temp()==18:
        salida1="El número "+str(con_operations.romano(valor)[0]) + "\na Romano es: "+str(con_operations.romano(valor)[1])

def process2(valor1,valor2):
    global salida1
    salida1=""
    if get_temp()==4:
        salida1="Dentro del grupo de estudiantes,\n el porcentaje de mujeres es de:\n " + str(seq_operations.porcentajes(valor1,valor2)[0]) + "% por lo que el\n de hombres será: " +str(seq_operations.porcentajes(valor1,valor2)[1]) +"%"
    if get_temp()==6:
        salida1="La equivalencia de pesos \ncolombianos a dólares es de: \n" + str(seq_operations.equivalencia(valor1,valor2))
    if get_temp()==15:
        salida1=str(con_operations.puls_genero(valor1,valor2))
    if get_temp()==17:
        salida1=str(con_operations.azar(valor1,valor2))
    if get_temp()==19:
        salida1=str(con_operations.descuento(valor1,valor2))
    if get_temp()==20:
        salida1=str(con_operations.balota(valor1,valor2))

def process3(valor1,valor2,valor3):
    global salida1
    salida1=""
    if get_temp()==10:
        salida1="El porcentaje de inversión del \n1 socio es de: "+ str(seq_operations.inversion(valor1,valor2,valor3)[0]) +"%, del 2 socio \nde: "+ str(seq_operations.inversion(valor1,valor2,valor3)[1]) +"% y del 3 socio \nde: " + str(seq_operations.inversion(valor1,valor2,valor3)[2]) + "%"
    if get_temp()==11: 
        salida1="La masa del aire es\n de: "+ str(seq_operations.masa(valor1,valor2,valor3))
    if get_temp()==13: 
        salida1=str(con_operations.articulo(valor1,valor2,valor3))  
    if get_temp()==21: 
        salida1=str(con_operations.operaciones(valor1,valor2,valor3)) 

def process4(valor1,valor2,valor3,valor4):
    global salida1
    salida1=""
    if get_temp()==1:
        salida1="El salario del vendedor es \nde: "+ str(seq_operations.vendedor(valor1,valor2,valor3,valor4))
    if get_temp()==22: 
        salida1=str(con_operations.nota(valor1,valor2,valor3,valor4))

def process5(valor1,valor2,valor3,valor4,valor5):
    global salida1
    salida1=""
    if get_temp()==3:
         salida1="La nota final del estudiante \nes de: " +str(seq_operations.aprendiz(valor1,valor2,valor3,valor4,valor5))

def process6(valor1,valor2,valor3,valor4,valor5,valor6):
    global salida1
    salida1=""
    if get_temp()==5:
         salida1="La edad de la persona \nes de: " +str(seq_operations.edad(valor1,valor2,valor3,valor4,valor5,valor6))