from abc import ABC,abstractmethod

class Beings(ABC):

    def __init__(self,kind,isAlive):
        self.kind=kind
        self.isAlive=isAlive

    @abstractmethod
    def introduce(self):
       pass
    
   