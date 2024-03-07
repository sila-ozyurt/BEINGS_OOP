from TransportVehicle import TransportVehicle


class Airplane(TransportVehicle):

    def __init__(self,kind,type,cargoCapacity,fuelType,tankState,airline,isAlive=False,material="unknown",color="unknown"):
        super().__init__(kind,type,cargoCapacity,fuelType,tankState,isAlive,material,color)
        self.airline=airline

    #override
    def introduce(self):
        print("kind: ",self.kind)
        print("type: ",self.type)
        print("cargoCapacity: ",self.cargoCapacity)
        print("fuelType: ",self.fuelType)
        print("tankState: ",self.tankState)
        print("material: ",self.material)
        print("color: ",self.color)
        print("airline: ",self.airline)


    #override
    def fillUpTank(self):
        if self.tankState==100:
            print("fuel tank is already full")
        else:
            self.tankState=100
            print("fuel tank filled up")

   
airplane1=Airplane("airplane","air vehicle",5000,"gasoline",40,"turkish airlines")
airplane1.introduce()
airplane1.fillUpTank()
airplane1.fillUpTank()
