from LivingBeings import LivingBeings
from abc import ABC,abstractmethod

class Animals(LivingBeings,ABC):

    def __init__(self,kind,age,predictedLifetime,habitat,carnivoreOrHerbivore,isAlive=True):
        super().__init__(kind,isAlive,age,predictedLifetime)
        self.habitat=habitat
        self.carnivoreOrHerbivore=carnivoreOrHerbivore

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
    def makeSound(self):
        pass

    @abstractmethod
    def move(self):
        pass


    
    