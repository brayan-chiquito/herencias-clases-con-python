class Banco:
    def __init__(self):
        self.cliente1=Cliente("Brayan")
        self.cliente2=Cliente("Alejo")
        self.cliente3=Cliente("Pepito")
 
    def __operacion(self):
        self.cliente1.setdepositar(2000)
        self.cliente2.setdepositar(600)
        self.cliente3.setdepositar(100)
        self.cliente1.setextraer(800)
 
    def __depositos(self):
        total=self.cliente1.getdevolver()+self.cliente2.getdevolver()+self.cliente3.getdevolver()
        print("El total de dinero del banco es: ",total)
        self.cliente1.getimprimir()
        self.cliente2.getimprimir()
        self.cliente3.getimprimir()
    
    def getoperacion(self):
        return self.__operacion()

    def getdeposito(self):
        return self.__depositos()

 
class Cliente:
    def __init__(self,nombre):
        self.nombre=nombre
        self.cantidad=0
 
    def __depositar(self,cantidad):
        self.cantidad+=cantidad
 
    def __extraer(self,cantidad):
        self.cantidad-=cantidad
 
    def __devolver_cantidad(self):
        return self.cantidad
 
    def __imprimir(self):
        print(self.nombre, " tiene depositada una cantidad de ",self.cantidad)

    def setdepositar(self,valor):
        self.__depositar(valor)

    def setextraer(self, valor1):
        self.__extraer(valor1)

    def getdevolver(self):
        return self.__devolver_cantidad()
    
    def getimprimir(self):
        return self.__imprimir()

banco = Banco()
banco.getoperacion()
banco.getdeposito()
    
