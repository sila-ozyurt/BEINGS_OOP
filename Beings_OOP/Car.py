from numpy import mat
from TransportVehicle import TransportVehicle


class Car(TransportVehicle):

    def __init__(self,kind,type,cargoCapacity,fuelType,tankState,brand,year,mileage,isAlive=False,material="unknown",color="unknown"):
        super().__init__(kind,type,cargoCapacity,fuelType,tankState,isAlive,material,color)
        self.brand=brand
        self.year=year
        self.mileage=min(max(int(mileage),0),100)

        

    #override
    def introduce(self):
        print("kind: ",self.kind)
        print("type: ",self.type)
        print("cargoCapacity: ",self.cargoCapacity)
        print("fuelType: ",self.fuelType)
        print("tankState: ",self.tankState)
        print("material: ",self.material)
        print("color: ",self.color)
        print("brand: ",self.brand)
        print("year: ",self.year)
        print("mileage: ",self.mileage)

    #override
    def fillUpTank(self):
        if self.tankState==100:
            print("fuel tank is already full")
        else:
            self.tankState=100
            print("fuel tank filled up")

   
# car1=Car("car","land vehicle","50kg","diesel fuel",80,"volvo",2012,180)
# car1.introduce()
# car1.fillUpTank()
# car1.fillUpTank()


