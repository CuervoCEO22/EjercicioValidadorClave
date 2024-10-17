from abc import ABC, abstractmethod 
#Librerias necesarias para crear clases y  métodos abstractos

class ReglaValidacion(ABC): #hereda de ABC para que sea una clase abstracta
    
    
    #Según el ejercicio:  el atributo _longitud_esperada, el cual es inicializado en el constructor de la clase e indica la longitud que la clave debe superar.
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada = longitud_esperada

    @abstractmethod #El decorador que indica los métodos abstractos
    def es_valida(self, clave: str) -> bool:
        pass 

    def _validar_longitud(self, clave: str,) -> bool:
        return len(clave) >= self.longitud_esperada




