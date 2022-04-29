class Planes:
    __codigoplan=''
    __modelo=''
    __version=''
    __valorvehiculo=''
    __cantcuotasdelplan=''
    __cantcuotasapagar=''
    
    def __init__(self,codigoplan,modelo,version,valorvehiculo,cantcuotasdelplan,cantcuotasapagar):
        self.__codigoplan=codigoplan
        self.__modelo=modelo
        self.__version=version
        self.__valorvehiculo=valorvehiculo
        self.__cantcuotasdelplan=cantcuotasdelplan
        self.__cantcuotasapagar=cantcuotasapagar
        
    def getCodigo(self):
        return self.__codigoplan
    
    def getModelo(self):
        return self.__modelo
    
    def getVersion(self):
        return self.__version
    
    def getValorvehiculo(self):
        return self.__valorvehiculo
    
    def getCantcuotasdelplan(self):
        return self.__cantcuotasdelplan
    
    def getCantcuotasapagar(self):
        return self.__cantcuotasapagar
    
    def actualizarvalor(self,valor):
        self.__valorvehiculo=valor
    
    def montoparalicitar(self):
        return (int(self.__cantcuotasdelplan)+int(self.__cantcuotasapaga))
    
    def actualizarcantcuotas(self,valor):
        self.__cantcuotasapagar=valor