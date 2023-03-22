"""
Ejercicio POO/OOP (Programacion Orientada a objetos):
https://ellibrodepython.com/programacion-orientada-a-objetos-python
"""

#Ejercicio 1
"""
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construye los siguientes métodos para la clase:
    - Un constructor, donde los datos pueden estar vacíos.
    - Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
    - mostrar(): Muestra los datos de la persona.
    - es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
"""

class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
            if type(nombre) == str:
                self.__nombre = nombre
            else: 
                print("Dato incorrecto")
              
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        if type(edad) == int:
            self.__edad = edad
        else:
            print("Dato incorrecto")
    
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        if type(dni) == int:
            self.__dni = dni
        else:
            print("Dato incorrecto")

    def mostrar(self):
        print(self.__nombre)
        print(self.__edad)
        print(self.__dni)
        
    def es_mayor_de_edad(self):
        if self.__edad >= 18:
            print("Es mayor de edad")
        else:
            print("no es mayor de edad")

persona = Persona()
persona.nombre = "panchop"
persona.edad = 18
persona.dni = 15123132
persona.mostrar()
persona.es_mayor_de_edad()
print("#"*20)

#Ejercicio 2
"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
    titular (que es una persona)
    cantidad (puede tener decimales)
El titular será obligatorio y la cantidad es opcional. 
Construye los siguientes métodos para la clase:
    - Un constructor, donde los datos pueden estar vacíos.
    - Los setters y getters para cada uno de los atributos.
      El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
    - mostrar(): Muestra los datos de la cuenta.
    - ingresar(cantidad): se ingresa una cantidad a la cuenta.
      si la cantidad introducida es negativa, no se hará nada.
    - retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
"""

class Cuenta():
    def __init__(self, titular):
        self.titular = titular
        self.__cantidad = None
    
    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        if cantidad < 0:
            print("monto invalido")
        else:
             self.__cantidad = cantidad
    
    def mostrar(self):
        print(self.titular.nombre)
        print(self.titular.edad)
        print(self.titular.dni)
        print(self.__cantidad)

    def ingresar(self, cantidad):
        cantidad = float(cantidad)
        self.__cantidad = cantidad

    def retirar (self, monto):
        monto = float(monto)
        self.__cantidad = self.__cantidad - monto
    
cuenta = Cuenta(persona)
cuenta.ingresar(20000)
cuenta.retirar(10000)
cuenta.mostrar()


#Ejercicio 3
"""
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que 
deriva de la anterior.
Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación
que estará expresada en tanto por ciento.

Construye los siguientes métodos para la clase:
    - Un constructor.
    - Los setters y getters para el nuevo atributo.
    - En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad.
      Por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad
      pero menor de 25 años y falso en caso contrario.
    - Además la retirada de dinero sólo se podrá hacer si el titular es válido.
    - El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
    - Piensa los métodos heredados de la clase madre que hay que reescribir.
"""

class CuentaJoven(Cuenta):
    def __init__(self, persona):
        super().__init__(persona)
        self.__bonificacion = None

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion 

    def ingresar(self, valor):
        super().ingresar(valor)
        print(self.cantidad, self.bonificacion)
        self.cantidad = self.cantidad + self.cantidad * self.bonificacion / 100 

    def es_titular_valido(self):
        es_joven = False
        if self.titular.edad in range(18, 25):
            es_joven = True
        return es_joven
    
    def retirar(self, valor):
        if self.es_titular_valido():
            super().retirar(valor)

    def mostrar(self):
        super().mostrar()
        if self.es_titular_valido():
            print("Cuenta Joven", self.bonificacion, "%")
            print(self.cantidad)
        else:
            print("cuenta joven no valida")

cuenta_joven = CuentaJoven(persona)
print(cuenta_joven.__dict__)
cuenta_joven.bonificacion = 10
cuenta_joven.ingresar(2000)
cuenta_joven.retirar(500)
cuenta_joven.mostrar()


        
        

            






