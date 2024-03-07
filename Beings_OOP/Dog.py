from Animals import Animals

class Dogs(Animals):

    def __init__(self,kind,age,predictedLifetime,habitat,carnivoreOrHerbivore,furColor,ownerName="doesn't have an owner",isAlive=True):
        super().__init__(kind,age,predictedLifetime,habitat,carnivoreOrHerbivore,isAlive)
        self.furColor=furColor
        self.ownerName=ownerName

    #override
    def introduce(self):
        print(self.age,"-year old ",self.kind)
        print("lives in ",self.habitat)
        print("it is ",self.carnivoreOrHerbivore)
        print("its fur is ",self.furColor)
        
        if self.ownerName!="doesn't have an owner":
            print("its owner name is ",self.ownerName)
        else:
            print(self.ownerName)
    

    #override
    def showAge(self):
        print("I am an",self.age,"-year old dog")

    #override
    def calculateRestOfTheLife(self):
        return self.predictedLifetime-self.age

    #override
    def makeSound(self):
        print("bark bark!!!")

    #override
    def move(self):
        print("I move with my four legs")


    
# dog1=Dogs("golden",4,14,"home","carnivore","yellow")
# print(dog1.age)
# dog1.introduce()
# dog1.showAge()
# print(dog1.calculateRestOfTheLife())
# dog1.makeSound()
# dog1.move()
