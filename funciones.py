
import csv
from collections import defaultdict
import requests
import os
from pprint import pprint


# Opcion N0
# Crear una funcion que imprima por pantalla el barrio de CABA con mas casos confirmados

def n00():
    with open("casos_covid19.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        counter = defaultdict(int)
        for i, row in enumerate(reader):
            # ignore the first row (column headers)
            if i == 0:
                continue
            # suppose we want to handle the second column, row[1] is the second column's value.
            col_val = row[5]
            # everytime we meet a column value, we increase the counter of it.
            counter[col_val] += 1
        # convert the counter from dict to list, so that we can sort it later.
        flat_counter = [(col_val, cnt) for col_val, cnt in counter.items()]
        # key argument tells "sorted" to sort on "cnt" of flat_counter's tuples
        rs = sorted(flat_counter, key=lambda x: x[1], reverse=True)
        # print the top 1
        for col_val, cnt in rs[:1]:
            print(col_val, cnt)

def n0():
    #creo dicc. barrios vacio
    barrios = {}
    with open("casos_covid19.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        #recorrer archivo csv completo
        for row in reader:
            #if 'provincia' es CABA
            if row[4] == "CABA":
                #si 'barrio' esta en lista de barrios
                if row[5] in barrios:
                    #sumo la cantidad de ese barrio + 1
                    barrios[row[5]] += 1       
                else:
                    #sino agrego el barrio al barrios y le asigno valor 1
                    barrios[row[5]] = 1
        max = 0
        for barrio in barrios:
            #recorro diccionario de barrios buscando el mayor
            if barrios[barrio] > max:
                max = barrios[barrio]
                #me guardo el barrio con mas casos
                barriomax = barrio
        print("El barrio con mas casos confirmados es : ", barriomax, "es : ",max)


# Opcion N1
# Crear una funcion que imprima por pantalla la cantidad de casos confirmados por cada barrio de CABA

def n1():
    barrios = {}
    with open("casos_covid19.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        for row in reader:
            if row[4] == "CABA":
                if row[5] in barrios:
                    barrios[row[5]] += 1
                else:
                    barrios[row[5]] = 1
        for barrio in barrios:
            cant = barrios[barrio]
            print(barrio, "Tiene : ", cant ,"de casos confirmados")


# Opcion N2
# Crear una funcion que reciba el nombre de un barrio de CABA como argumento e imprima por pantalla la cantidad de casos

def n2():
    barrios = {}
    with open("casos_covid19.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        for row in reader:
            if row[4] == "CABA":
                if row[5] in barrios:
                    barrios[row[5]] += 1
                else:
                    barrios[row[5]] = 1
    #leo primer barrio
    barrio_act = input("Ingrese barrio")
    while barrio_act not in barrios:
        #si no esta en barrios, leo nuevamente
        print("Barrio incorrecto, ingrese nuevamente")
        barrio_act = input("Ingrese barrio: ")
    #recorro los barrios buscando e informando la cantida de casos
    for barrio in barrios:
        if barrio in barrios:   #esta de mas?
            if barrio == barrio_act:
                print("Cantidad de casos : ", barrios[barrio])

# Opcion N3
# Crear una funcion que imprima por pantalla la cantidad de casos totales separados por GBA y CABA

def n3():
    GBA = {}
    CABA = {}
    with open("casos_covid19.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        for row in reader:
            #recorro el archivo agregando los barrios a sus respectivos dic. sumando sus casos confirmados
            if row[4] == "CABA":
                if row[5] in CABA:
                    CABA[row[5]] += 1
                else:
                    CABA[row[5]] = 1
            if row[4] == "Buenos Aires":
                if row[5] in GBA:
                    GBA[row[5]] += 1
                else:
                    GBA[row[5]] = 1
    #sumo el total de casos en GBA y CABA
    totalGBA = 0
    totalCABA = 0
    for barrio in GBA:
        cantidad = GBA[barrio]
        totalGBA = totalGBA + cantidad
    for barrio in CABA:
        cantidad = CABA[barrio]
        totalCABA = totalCABA + cantidad
    print("GBA tiene : ", totalGBA, "de casos confirmados")
    print("CABA tiene : ", totalCABA, "de casos confirmados")

# Opcion N4
# Crear una funcion que reciba "total", CABA" o "GBA" como argumento y imprima por pantalla la cantidad total de casos segun genero teniendo en cuenta el argumento especificado

def n4():
    GBA = {}
    CABA = {}
    with open("casos_covid19.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        for row in reader:
            #recorro el archivo agregando los barrios a sus respectivos dic. sumando sus casos confirmados
            if row[4] == "CABA":
                if row[5] in CABA:
                    CABA[row[5]] += 1
                else:
                    CABA[row[5]] = 1
            if row[4] == "Buenos Aires":
                if row[5] in GBA:
                    GBA[row[5]] += 1
                else:
                    GBA[row[5]] = 1
    #sumo el total de casos en GBA y CABA
    total = 0
    totalGBA = 0
    totalCABA = 0
    for barrio in GBA:
        cantidad = GBA[barrio]
        totalGBA = totalGBA + cantidad
    for barrio in CABA:
        cantidad = CABA[barrio]
        totalCABA = totalCABA + cantidad
    total = totalCABA + totalGBA
    #primera lectura
    info = input("Elija opcion : CABA - GBA - TOTAL: ")
    while True:
        if info == "CABA":
            print("Cantidad de casos en CABA : ", totalCABA)
            break
        elif info == "GBA":
            print("Cantidad de casos en GBA : ", totalGBA)
            break
        elif info == "TOTAL":
            print("Cantidad de casos totales : ", total)
            break
        else:
             info = input ("Opcion incorrecta, seleccione nuevamente : CABA - GBA - TOTAL: ")
        continue

# Opcion N5
# Crear una funcion que cree un diccionario CASOS_DE_COVID utilizando el archivo que descargamos anteriormente:
# https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-salud/casos-covid-19/casos_covid19.csv
# Luego de crear el diccionario imprimirlo por pantalla

def n5():
    CASOS_DE_COVID = {}
    with open("casos_covid19.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        for row in reader:
            if row[4] not in CASOS_DE_COVID:
                CASOS_DE_COVID[row[4]] = 1
            else:
                CASOS_DE_COVID[row[4]] += 1
    pprint(CASOS_DE_COVID)
 

# Opcion N6
# Crear una funcion que detecte si el archivo (casos_covid19.csv) esta en la carpeta donde estamos ejecutando el script y de no encontrarlo lo descargue.
# Nota: Para realizar pedidos HTTP en Python utilizar el modulo requests, el cual requerira instalarlo utilizando PIP3


def n6():
    url = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-salud/casos-covid-19/casos_covid19.csv"
    if os.path.isfile("casos_covid19.csv"): 
        with open("casos_covid19.csv") as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            print("Archivo encontrado")
    else:
        print("Archivo no encontrado, descargando...")
        data = requests.get(url)
        open("casos_covid19.csv", 'wb').write(data.content)

    """try:
        with open("casos_covid19.csv") as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            print("Archivo encontrado")

    except FileNotFoundError:
        print("Archivo no encontrado, descargando...")
        data = requests.get(url)
        open("casos_covid19.csv", 'wb').write(data.content)
   """
    
# Opcion N7
# Crear una funcion que printee una lista con los barrios de CABA que tengan mas de 10.000 casos confirmados.

def n7():
    barrios = {}
    with open("casos_covid19.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        for row in reader:
            if(row[4]) == "CABA":
                if row[5] in barrios:
                    barrios[row[5]] += 1
                else:
                    barrios[row[5]] = 1
    for barrio in barrios:
        if barrio == "NA":
            continue
        elif barrios[barrio] > 10000:
            print(barrio)

    

    


   

            

 


    





               

               
                








    

        
    






            



            


            

            


    

   




