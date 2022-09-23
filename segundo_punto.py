class Persona:
    def __iniciar(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    def __mostrar(self):
        print("nombre: ", self._nombre)
        print("edad: ", self._edad)
    
    def __comprobar_edad(self):
        if self._edad >= 18:
            print("es mayor de edad")
        else:
            print("es menor de edad")
    
    def setiniciar(self, nombre1 , edad1):
        self.__iniciar(nombre1, edad1)

    def getmostrar(self):
        return self.__mostrar()

    def getcomprobar(self):
        return self.__comprobar_edad()

perso1 = Persona()
perso2 = Persona()
perso3 = Persona()

perso1.setiniciar("brayan",24)
perso2.setiniciar("alejo",13)

perso1.getmostrar()
perso1.getcomprobar()
perso2.getmostrar()
perso2.getcomprobar()









