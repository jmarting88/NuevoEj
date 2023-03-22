"""
Ejercicio modulos:
Crear un programa que en su archivo "main.py" tenga un menu con las siguientes opciones:
Para los datos vamos a utilizar el csv: https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-salud/casos-covid-19/casos_covid19.csv
Para leer archivos csv: https://realpython.com/python-csv/
"""

import csv
from funciones import n0,n1,n2,n3,n4,n5,n6,n7

def main():
    opciones = {"0":n0, "1":n1, "2":n2, "3":n3, "4":n4, "5":n5, "6":n6, "7":n7}
    while True:
        opcion=input("Elija opcion: ")
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("opcion incorrecta")
            

        
if __name__ == "__main__":
    main()
