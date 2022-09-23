class Triangulo:
    def __iniciar(self):
        self._lado1 = input("lado 1: ")
        self._lado2 = input("lado 2: ")
        self._lado3 = input("lado 3: ")
    
    def __mostrar(self):
        print("lado 1: ",self._lado1)
        print("lado 2: ",self._lado2)
        print("lado 3: ",self._lado3)

    def __mayor(self):
        print("lado mayor...")
        if self._lado1>self._lado2 and self._lado1>self._lado3:
            print("lado 1: ", self._lado1)
        elif self._lado2>self._lado3:
            print("lado 2:", self._lado2)
        else:
            print("lado 3: ", self._lado3)
    
    def __tipo(self):
        if self._lado1==self._lado3:
            print("es equilatero")
        elif self._lado1!=self._lado2 and self._lado1!=self._lado3:
            print("es escaleno")
        else:
            print("es isosceles")

    def setiniciar(self):
        return self.__iniciar()
    
    def getmostrar(self):
        return self.__mostrar()
        
    def getmayor(self):
        return self.__mayor()
    
    def gettipo(self):
        return self.__tipo()

forma = Triangulo()
forma.setiniciar()
forma.getmostrar()
forma.getmayor()
forma.gettipo()
    
