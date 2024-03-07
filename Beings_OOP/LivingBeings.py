from Beings import Beings
from abc import ABC,abstractmethod

class LivingBeings(Beings,ABC):

    def __init__(self,kind,isAlive,age,predictedLifetime):
        super().__init__(kind,isAlive)
        self.age=age
        self.predictedLifetime=predictedLifetime

    #override
    def introduce(self):
        pass
    
    @abstractmethod
    def showAge(self):
        pass
    
    @abstractmethod
    def calculateRestOfTheLife(self):
        pass
    

