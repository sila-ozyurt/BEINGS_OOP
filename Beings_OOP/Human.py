from LivingBeings import LivingBeings
from abc import ABC,abstractmethod

class Human(LivingBeings,ABC):

    def __init__(self,kind,isAlive,age,name,surname,weight,occupation,predictedLifetime=80,isMarried="single"):
        super().__init__(kind,isAlive,age,predictedLifetime)
        self.name=name
        self.surname=surname
        self.weight=weight
        self.occupation=occupation
        self.isMarried=isMarried
        

    #override
    def introduce(self):
        pass
    
    #override
    def showAge(self):
        pass

    #override
    def calculateRestOfTheLife(self):
        pass

    @abstractmethod
    def marryHuman(self):
        pass
