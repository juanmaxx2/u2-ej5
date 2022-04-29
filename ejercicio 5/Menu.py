class Menu:
    opcion=None
    def __init__(self):
        self.__opcion=None
    def mostrarmenu(self,Manejador):
        while self.__opcion!=-1:
            print('1) para actualizar el valor de los autos')
            print('2) ingresar valor para mostrar datos')
            print('3) mostrar el valor para licitar el vehiculo')
            print('4) ingrese el codigo del plan, para modificar la cantidad de cuotas')
            self.__opcion=input('Ingrese numero: ')
            if self.__opcion=='1':
                Manejador.Actualizar()
                
            elif self.__opcion=='2':
                valor=int(input('\nIngrese el valor a comparar con las cuotas:'))
                Manejador.Mostrarvalor(valor)
            
            elif self.__opcion=='3':
                
            
            elif self.__opcion=='4':
                codigo=int(input('\nIngrese el codigo de plan a modificar:'))
                Manejador.Actcantcuotas(codigo)