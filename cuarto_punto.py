class Operaciones:
    def __init__(self):
        self._valor1 = int(input("primer valor: "))
        self._valor2 = int(input("segundo valor: "))
 
    def __suma(self):
        suma=self._valor1+self._valor2
        print("la suma es: ",suma)
 
    def __resta(self):
        resta=self._valor1-self._valor2
        print("la resta es: ",resta)
 
    def __multiplicacion(self):
        pro=self._valor1*self._valor2
        print("la multiplicación es: ",pro)
 
    def __division(self):
        div=self._valor1/self._valor2
        print("la división es: ",div)
 
    def __imprimir(self):
        print("Valor 1: ",self._valor1)
        print("Valor 2: ",self._valor2)

    def getsuma(self):
        return self.__suma()

    def getresta(self):
        return self.__resta()

    def getmultiplicacion(self):
        return self.__multiplicacion()

    def getdivision(self):
        return self.__division()
    
    def getmostrar(self):
        return self.__imprimir()
    
calcu = Operaciones()
calcu.getmostrar()
calcu.getsuma()
calcu.getresta()
calcu.getmultiplicacion()
calcu.getdivision()

    
