from NonlivingBeings import NonlivingBeings
from abc import ABC,abstractmethod

class TransportVehicle(NonlivingBeings,ABC):

    def __init__(self,kind,type,cargoCapacity,fuelType,tankState,isAlive=False,material="unknown",color="unknown"):
        super().__init__(kind,isAlive,material,color)
        self.type=type
        self.cargoCapacity=cargoCapacity
        self.fuelType=fuelType
        self.tankState=min(max(int(tankState),0),100) 

    #override
    def introduce(self):
        pass

    @abstractmethod
    def fillUpTank(self):
        pass

   



    