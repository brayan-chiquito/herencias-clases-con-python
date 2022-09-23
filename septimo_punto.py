class Cuenta:
    def __init__(self,titular,cantidad):
        self.titular=titular
        self.cantidad=cantidad
 
    def __imprimir(self):
        print("Titular: ",self.titular)
        print("Cantidad: ", self.cantidad)
    
    def getmostrar1(self):
        return self.__imprimir()

class CajaAhorro(Cuenta):
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
 
    def __imprimir(self):
        print("Cuenta de caja de ahorros")
        super().getmostrar1()

    def getmostrar2(self):
        return self.__imprimir()
 
class PlazoFijo(Cuenta):
    def __init__(self,titular,cantidad,plazo,interes):
        super().__init__(titular,cantidad)
        self.plazo=plazo
        self.interes=interes
 
    def __ganancia(self):
        ganancia=self.cantidad*self.interes/100
        print("El importe de interés es: ",ganancia)

    def __imprimir(self):
        print("Cuenta a plazo fijo")
        super().getmostrar1()
        print("Plazo disponible en días: ",self.plazo)
        print("Interés: ",self.interes)
        self.__ganancia()

    def getganancia(self):
        return self.__ganancia()

    def getimprimir(self):
        return self.__imprimir()

caja = CajaAhorro("brayan",50000)
caja.getmostrar2()

plazo = PlazoFijo("alejo", 10000, 365, 2.5)
plazo.getimprimir()