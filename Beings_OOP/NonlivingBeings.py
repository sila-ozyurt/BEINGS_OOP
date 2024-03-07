from Beings import Beings
from abc import ABC,abstractmethod

class NonlivingBeings(Beings,ABC):

    def __init__(self,kind,isAlive=False,material="unknown",color="unknown"):
        super().__init__(kind,isAlive)
        self.material=material
        self.color=color

     
    #override
    def introduce(self):
        pass
