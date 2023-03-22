# Ejercicio 1
# Escribir un funcion que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
# Para realizar este ejercicio necesitamos conocer la funcion nativa de python input()
# Documentacion --> https://www.w3schools.com/python/ref_func_input.asp
# Tener en cuenta que la funcion input retorna un string, por lo que tenemos que convertirlo a entero(int)

import string


def funcion1():
    edad = int(input("Ingrese edad "))
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")


#funcion1()

# Ejercicio 2
# Escribir una funcion que pida al usuario una palabra y la muestre por pantalla 10 veces.

def funcion2():
    palabra = input("Ingrese palabra ")
    for i in range(0, 10):
        print(palabra)

#funcion2()

# Ejercicio 3
# Escribir un funcion que pregunte al usuario un número que represente un mes, escribir el nombre del mes correspondiente.
# Para realizar este ejercicio tenemos que utilizar los indices de una lista: 
# Documentacion --> https://www.programiz.com/python-programming/list
# Puede haber error en el número dado.

def funcion3():
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    mes = int (input("Ingrese mes"))
    if mes < 1 or mes > 12:
        print("Mes ingresado no valido")
    else:
        print("El mes es:", meses[mes-1])

# funcion3()


# Ejercicio 4
# Escribir una funcion que pida al usuario ingresar tres números. La funcion debera hallar el mayor numero y lo muestrarlo por pantalla.

def funcion4():
    nro1 = int (input("ingrese primer nro"))
    nro2 = int (input("ingrese segundo nro"))
    nro3 = int (input("ingrese tercer nro"))
    if nro1 > nro2 and nro1 > nro3:
        print(nro1)
    elif nro2 > nro1 and nro2 > nro3:
        print(nro2)
    else:
        print(nro3)

#funcion4()

# Ejercicio 5
# Escribir una funcion que almacene la cadena de caracteres "contraseña" en una variable
# Pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada 
# sin tener en cuenta mayúsculas y minúsculas.

def funcion5():
    cadena = "contraseña"
    password = input("Ingrese contraseña")
    if cadena == password:
        print("La contraseña es correcta")
    else:
        print("Contraseña incorrecta")

#funcion5()


# Ejercicio 6
# Teniendo la siguiente lista de barrios:
# barrios_caba = ["Barrios", "Agronomía", "Almagro", "Balvanera", "Barracas", "Belgrano", "Boedo", "Caballito", "Chacarita", "Coghlan"]
# Escribir una funcion que muestre por pantalla los barrios que incien con las letras "ba"
# Para realizar este ej. podemos utilizar el metodo .startswith("Ba") de los objetos de tipo string: string.startswith("Ba")
# Documentacion --> https://www.w3schools.com/python/ref_string_startswith.asp

def funcion6():
    barrios_caba = ["Barrios", "Agronomía", "Almagro", "Balvanera", "Barracas", "Belgrano", "Boedo", "Caballito", "Chacarita", "Coghlan"]
    for barrio in barrios_caba:
        if barrio.startswith("Ba"):   
            print(barrio)

#funcion6()

# Ejercicio 7
# Escribir una funcion para hallar la superficie de un triangulo conociendo la base y la altura.
# El programa tiene que solcitar al usuario que ingrese la base y la altura.
# Superficie = base * altura / 2

def funcion7():
    base = int(input("ingrese base: "))
    altura = int(input("ingrese altura"))
    print("La superficie es:", base * altura / 2)

#funcion7()

# Ejercicio 8
# Escribir una funcion que pida al usuario dos números y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.

def funcion8():
    numerador = int (input("ingrese numerador"))
    denominador = int (input("ingrese denominador"))
    if denominador == 0:
        print("Error")
    else:
        print(numerador/denominador)

#funcion8()

# Ejercicio 9
# Volvemos a utilizar la lista de barrios:
# barrios_caba = ["Barrios", "Agronomía", "Almagro", "Balvanera", "Barracas", "Belgrano", "Boedo", "Caballito", "Chacarita", "Coghlan"]
# Escribir un programa que muestre por pantalla todos los barrios dentro de la lista pero en mayuscula
# Para realizar este ej. podemos utilizar el metodo .upper() de los objetos de tipo string string.upper() 
# Documentacion --> https://www.w3schools.com/python/ref_string_upper.asp

def funcion9():
    barrios_caba = ["Barrios", "Agronomía", "Almagro", "Balvanera", "Barracas", "Belgrano", "Boedo", "Caballito", "Chacarita", "Coghlan"]
    for barrio in barrios_caba:
        print(barrio.upper())

#funcion9()

# Ejercicio 10
# Escribir una funcion que pida al usuario un número entero y muestre por pantalla si es par o impar.

def funcion10():
    numero = int(input("Ingrese un numero"))
    if numero != 0:
        if numero % 2 == 0:
            print("Es par")
        else:
            print("Es impar")
    else:
        print("Ingrese numero distinto de cero")

#funcion10()
    



# Ejercicio 11
# Dada la siguiente lista de frutas:
# frutas = ["manzana", "banana", "pera", "anana"]
# Escribir un programa que le solicite al usuario una fruta y verifique si esta existe dentro de la lista de frutas.
# Para realizar este ejercicio podemos utilizar la palabra reservada in.
# Documentacion --> https://www.w3schools.com/python/ref_keyword_in.asp

def funcion11():
    frutas = ["manzana", "banana", "pera", "anana"]
    fruta = input("Ingrese fruta")
    if fruta in frutas:
        print(fruta)
    else:
        print(fruta, "no esta en la lista")

#funcion11()


# Ejercicio 12
# Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores a $300.000 mensuales.
# Escribir una funcion que pregunte al usuario su edad, sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def funcion12():
    edad = int(input("ingrese edad"))
    if edad < 18:
        print("No tiene que tributar")
    else:
        ingresos = int(input("Ingrese cant. ingresos mensuales"))
        if ingresos >= 300000:
            print("Tiene que tributar")
        else:
            print("no tiene que tributar")
     
#funcion12()


# Ejercicio 13
# Escribir una funcion que pida al usuario una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas)

def funcion13():
    vocal = ['a', 'e', 'i', 'o', 'u']
    lista = []
    frase = input("Ingrese una frase")
    for letra in frase:
        if letra in vocal and letra not in lista:
            lista.append(letra)
    print(lista)

#funcion13()
        

# Ejercicio 14
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
# Escribir una funcion que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

def funcion14():
    nombre = input("Ingrese nombre")
    sexo = input("ingrese sexo")
    if sexo == 'M' and nombre[0].lower() > 'n': 
        print("Pertenece al grupo A")
    elif sexo == 'F' and nombre[0].lower() < 'm':
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")

#funcion14()
    

# Ejercicio 15
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# 			Renta					Tipo impositivo
#		Menos de 10000€					5%
#		Entre 10000€ y 20000€			15%
#		Entre 20000€ y 35000€			20%
#		Entre 35000€ y 60000€			30%
#		Más de 60000€					45%
# Escribir una funcion que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

def funcion15():
    ingreso=int(input("Declare ingresos anuales"))
    if ingreso < 10000:
        print("Debe pagar '5%' anual")
    elif ingreso >= 10000 and ingreso < 20000:
        print("Debe pagar '15%' anual")
    elif ingreso >= 20000 and ingreso < 35000:
        print("Debe pagar '20%' anual")
    elif ingreso >= 35000 and ingreso < 60000:
        print("Debe pagar '30%' anual")
    else:
        print("Debe pagar '45%' anual")

#funcion15()
    

# Ejercicio 16
# Escribir una funcion que pida al usuario un número entero positivo
# y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
# Para realizar este ej. podemos utilizar la funcion nativa de python range(start, stop, step).
# Documentacion --> https://www.w3schools.com/python/ref_func_range.asp 
# La funcion range utiliza 2 variables numericas start, stop como incio y fin.
# La tercer variable tambien numerica step especifica el incremento.

def funcion16():
    lista = []
    numero = int(input("ingrese un numero entero positivo"))
    if numero <= 0:
        print("Numero invalido")    #preg
    else:
        numero = range(1, numero, 2)
        for n in numero:
            lista.append(n)
        print(lista)
            
#funcion16()


# Ejercicio 17
# En una determinada empresa, sus empleados son evaluados al final de cada año.
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios.
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
#			Nivel					Puntuación
#		Inaceptable						0.0
#		Aceptable						0.4
#		Meritorio						0.6 o más
# La cantidad de dinero conseguida en cada nivel es de $100.000 multiplicada por la puntuación del nivel.
# Escribir una funcion que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

def funcion17():
    usuario = input("Ingrese nombre de usuario")
    puntuacion = float(input("Ingrese puntuacion"))
    if puntuacion == 0.0:
        print("Nivel de rendimiento : Inaceptable", "Corresponde :", 100000*puntuacion)
    elif puntuacion == 0.4:
        print("Nivel de rendimiento : Aceptable", "Corresponde :", 100000*puntuacion)
    elif puntuacion >= 0.6:
        print("Nivel de rendimiento : Meritorio", "Corresponde :", 100000*puntuacion)
    else:
        print("Puntuacion incorrecta")

    
    
#funcion17()


# Ejercicio 18
# Escribir una funcion que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def funcion18():
    edad = int(input("ingrese su edad"))
    edad = range(1, edad+1)
    for n in edad:
        print(n)

#funcion18()


# Ejercicio 19
# Escribir una funcion para una empresa que tiene salas de juegos para todas las edades 
# y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $1200 y si es mayor de 18 años, $2000.

def funcion19():
    edad = int(input("ingrese su edad"))
    if edad < 4:
        print("Ingresa gratis")
    elif edad >=4 and edad < 18:
        print("La entrada cuesta $1200")
    else:
        print("La entrada cuesta $2000")

#funcion19()

# Ejercicio 20
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# 		- Ingredientes vegetarianos: Morron y tofu.
#		- Ingredientes no vegetarianos: Longaniza, Jamón y Salmón.
# Escribir una funcion que pregunte al usuario si quiere una pizza vegetariana o no
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

def funcion20():
    pizza = ['tomate', 'muzza']
    vegetariano = ['morron', 'tofu']
    no_vegetariano = ["longaniza", "salmon", "jamon"]
    pedido = input("Desea pizza vegetariana?")   
    if not pedido in ["si", "no"]: 
        print("Ingrese pizza correcta")
    elif pedido == "si":
        print("Menu vegetariano:", vegetariano)
        ingrediente = input("Seleccione ingrediente extra")
        if ingrediente != "tofu" and ingrediente != "morron":  #se puede comparar si el ingrediente exisiste en la lista?
            print("Ingrediente no existe")
        else:
            pizza.append(ingrediente)
            print("Pizza vegetariana:", "Ingredientes", pizza)
    else:
        print("Menu No-Vegetariano:", no_vegetariano)
        ingrediente = input("Seleccione ingrediente extra")
        if ingrediente != "longaniza" and ingrediente != "salmon" and ingrediente != "jamon":
            print("ingrediente no existente")
        else:
            pizza.append(ingrediente)
            print("Pizza  No-Vegetariana:", "Ingredientes", pizza)

#funcion20()


# Ejercicio 21
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
# Para realizar este ejercicio tenemos que entender los indices de un objeto iterable
# Documentacion --> https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3

def funcion21():
    palabra = input("Ingrese palabra")
    for letra in palabra[::-1]:
        print(letra)

#funcion21()



# EJercicios While --> https://www.tutorialspoint.com/python3/python_while_loop.htm


# Ejercicio 1
"""
Escriba una funcion que le pida al usuario un número entero
y que compruebe si el número es menor que 10.
Si no lo es, debe volver a leer el número repitiendo la operación hasta que el usuario escriba un valor correcto.
Finalmente, debe escribir por pantalla el valor leído cuando este sea correcto.
"""

def ejercicio1():
    numero = int(input("Ingrese un numero"))
    while numero > 9:
        print("valor incorrecto")
        numero = int(input("Ingrese un numero"))
    print(numero)

#ejercicio1()


# Ejercicio 2
"""
Modifique la funcion del ejercicio anterior para que, en vez de comprobar que el número sea menor que 10, compruebe que se encuentre en el rango 0 a 20.
"""

def ejercicio2():
    numero = int(input("Ingrese un numero"))
    while numero in range(0,20):
        print("valor incorrecto")
        numero = int(input("Ingrese un numero"))
    print(numero)

#ejercicio2()


# Ejercicio 3
"""
Modifique la funcion del ejercicio anterior para que cuente las veces que ha leído un número de teclado y escriba el resultado por pantalla.
"""
def ejercicio3():
    numero = int(input("Ingrese un numero"))
    cantidad = 1
    while numero in range(0,20):
        cantidad += 1   #cantidad = cantidad+1
        print("valor incorrecto")
        numero = int(input("Ingrese un numero"))
    print(cantidad)
    

#ejercicio3()

#Ejercicio 4
"""
Modifique la funcion del ejercicio anterior para que se realicen 5 lecturas por teclado como máximo.
Documentacion --> https://www.ionos.com/digitalguide/websites/web-development/python-break-continue/
"""
def ejercicio4():
    numero = int(input("Ingrese un numero"))
    cantidad = 1
    while numero in range(0,20) and cantidad < 5:
        cantidad += 1
        print("valor incorrecto")
        numero = int(input("Ingrese un numero"))
    print(cantidad)

#ejercicio4()


#Ejercicio 5
"""
Escriba una funcion que calcule e imprima la suma de los n primeros números enteros positivos.
El valor de n debe leerse del teclado y ser ingresado por el usuario.
"""

def ejercicio5():
    suma = 0
    n = int(input("ingrese un numero"))
    i = 1
    while n > 0 and i <= n: #n=3 y i=4   suma=6
        suma = suma+i
        i = i+1
    print(suma)

#ejercicio5()



#Ejercicios Diccionarios --> https://ellibrodepython.com/diccionarios-en-python

#Ejercicio 1
"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}.
Preguntar al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

"""

def dic1():
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    divisa = input("Ingrese divisa").capitalize()  #.capitalize convierte el primer caracter igresado por el ususuario en mayuscula 
    if divisa in divisas:
        print(divisas[divisa])
    else:
        print("La divisa no esta disponible")

#dic1()
    

#Ejercicio 2
"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

"""
def dic2():
    nombre = input("Nombre")
    edad = int(input("Edad"))
    direccion = input("Direccion")
    telefono = int(input("Telefono"))
    datos = {'Nombre':nombre, 'Edad':edad, 'Direccion':direccion, 'Telefono':telefono} #creo el diccionario con los datos que ingresó el usuario
    print(datos['Nombre'], "Tiene", datos['Edad'],"años","Vive en ", datos["Direccion"], "y su numero de telefono es : ", datos["Telefono"])

#dic2()



#Ejercicio 3
"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla.
Preguntar al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
    Fruta	    Precio
    Plátano	    1.35
    Manzana	    0.80
    Pera	    0.85
    Naranja	    0.70
"""

def dic3():
    frutas = {'Plátano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja':0.70}
    fruta = input("ingrese fruta")
    kg = int(input("cantidad de kg"))
    if fruta in frutas:
        print("Precio : ", kg*frutas[fruta])
    else:
        print("fruta no disponible")

#dic3()


#Ejercicio 4
"""
Ejercicio 4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""

def dic4():
    meses = {1:'Enero', 2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}
    dd = int(input("Dia"))
    mm = int(input("Mes"))
    aaaa = int(input("Año"))
    print(dd,"de",meses[mm],"de",aaaa)
#dic4()


#Ejercicio 5
"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} 
Después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, 
donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
Al final debe mostrar también el número total de créditos del curso.
"""

def dic5():
    total = 0
    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    for asignatura in asignaturas:
        print(asignatura, "tiene",asignaturas[asignatura], "creditos")  
        total = total + asignaturas[asignatura]
    print("Numero de creditos del curso", total)

#dic5()