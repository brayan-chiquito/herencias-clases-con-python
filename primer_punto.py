#clase
class Alumno:
    def __iniciar(self, nombre , nota):
        self._nombre = nombre
        self._nota = nota
  
    def __mostrar(self):
        print("nombre: ", self._nombre)
        print("nota: ", self._nota)

    def __estado(self):
        if self._nota >= 3:
            print("aprovado")
        else:
            print("no aprovado")

    def setiniciar(self, nombre1, nota1):
        self.__iniciar(nombre1, nota1)

    def getmostrar(self):
        return self.__mostrar()
    
    def getestado(self):
        return self.__estado()

estu1=Alumno()
estu2=Alumno()
estu3=Alumno()

estu1.setiniciar("brayan",4)
estu2.setiniciar("alejo",3)
estu3.setiniciar("pepito",2.5)

estu1.getmostrar()
estu1.getestado()
estu2.getmostrar()
estu2.getestado()
estu3.getmostrar()
estu3.getestado()

