from PlanesAhorro import Planes
import csv
class Manejador:
    __lista=[]
    def __init__(self):
        self.iniciar()
        
    def iniciar(self):
        archivo=open('planes.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            Auto=Planes(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__lista.append(Auto)
    
    def Actualizar(self):
        for i in range(len(self.__lista)):
            print('\n El modelo de auto es:', format(self.__lista[i].getModelo()))
            print('\n La version del auto es:', format(self.__lista[i].getVersion()))
            print('\n El valor del auto es:', format(self.__lista[i].getValorvehiculo()))
            nuevovalor=input('/n Ingrese el nuevo valor del vehiculo:')
            self.__lista[i].actualizarvalor(nuevovalor)
    
    def Mostrarvalor(self,valor):        
        for i in range(len(self.__lista)):
            if valor<int(self.__lista[i].getCantcuotasapagar()):
                print('\n El modelo de auto es:', format(self.__lista[i].getModelo()))
                print('\n La version del auto es:', format(self.__lista[i].getVersion()))  
                print('\n El codigo de plan es:', format(self.__lista[i].getCodigo()))
    
    def Mostrarmontolicitar(self):
        for i in range(len(self.__lista)):
            self.__lista[i].montoparalicitar
    
    def Actcantcuotas(self,codigo):
        for i in range(len(self.__lista)):
            if codigo==self.__lista[i].getCodigo():
                nuevovalor=input('\n Ingrese la cantidad de cuotas que tiene que pagar:')
                self.__lista[i].actualizarcantcuotas(nuevovalor)