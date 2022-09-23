class Agenda:
    def __init__(self):
        self.contactos=[]

    def __menu(self):
        print()
        menu=[
            ['Agenda'],
            ['1. Añadir Contacto'],
            ['2. Lista de contactos'],
            ['3. Buscar contacto'],
            ['4. Editar contacto'],
            ['5. Cerrar agenda']
        ]

        for x in range(6):
            print(menu[x][0])
 
        opcion=int(input("Introduzca opción: "))
        if opcion==1:
            self.__anadir()
        elif opcion==2:
            self.__lista()
        elif opcion==3:
            self.__buscar()
        elif opcion==4:
            self.__editar()
        elif opcion==5:
            print("Saliendo de la agenda ...")
            exit()
        self.__menu()
 
    def __anadir(self):
        print("\n*********************")
        print("Añadir nuevo contacto")
        print("*********************")
        nom=input("nombre: ")
        telf=int(input("teléfono: "))
        email=input("email: ")
        self.contactos.append({'nombre':nom,'telf':telf,'email':email})
        
    def __lista(self):
        print("******************")
        print("Lista de contactos")
        print("******************")
        if len(self.contactos) == 0:
            print("No hay ningún contacto en la agenda")
        else:
            for x in range(len(self.contactos)):
                print(self.contactos[x]['nombre'])
        
    def __buscar(self):
        print("*********************")
        print("Buscador de contactos")
        print("*********************")
        nom=input("nombre del contacto: ")
        for x in range(len(self.contactos)):
            if nom == self.contactos[x]['nombre']:
                print("contacto")
                print("Nombre: ",self.contactos[x]['nombre'])
                print("Teléfono: ",self.contactos[x]['telf'])
                print("E-mail: ",self.contactos[x]['email'])
                return x
        
    def __editar(self):
        print("***************")
        print("Editar contacto")
        print("***************")
        data=self.buscar()
        condition=False
        while condition==False:
            print("elija que quiere editar: ")
            print("1. Nombre")
            print("2. Teléfono")
            print("3. E-mail")
            print("4. Volver")
            option=int(input("Introduzca la opción deseada: "))
            if option==1:
                nom=input("Introduzca nombre: ")
                self.contactos[data]['nombre']=nom
            elif option==2:
                telf=input("Introduzca teléfono: ")
                self.contactos[data]['telf']=telf
            elif option==3:
                email=input("Introduzca email: ")
                self.contactos[data]['email']=email
            elif option==4:
                condition=True
    def setmenu(self):
        return self.__menu()

agen = Agenda()
agen.setmenu()