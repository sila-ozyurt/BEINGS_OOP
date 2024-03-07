from Human import Human


class Woman(Human):

    def __init__(self,age,name,surname,weight,occupation,hobbies,kind="human",isAlive=True,predictedLifetime=80,isMarried="single"):
        super().__init__(kind,isAlive,age,name,surname,weight,occupation,predictedLifetime,isMarried)
        self.hobbies=hobbies if hobbies is not None else [] 
        
    #override
    def introduce(self):
        print("Hi I am ",self.name," ",self.surname,", a ",self.age,"-year old woman")
        print("I weigh ",self.weight)
        print("I am ",self.occupation)

        if len(self.hobbies)==0:
            print("I don't have any hobby, please help me a get one ")
        else:
            for i in self.hobbies:
                print("I like ",i)

    #override
    def showAge(self):
        print("I am a ",self.age,"-year old woman")
    
    #override
    def calculateRestOfTheLife(self):
        return self.predictedLifetime-self.age

    #override
    def marryHuman(self):
        if self.isMarried.lower()=="single":
            self.isMarried="married"
            print("I got married!!")
        else:
            print("I am already married!!!")
    
    def getAHobby(self,hobby):
        self.hobbies.append(hobby)

    def showHobbies(self):
        for i in self.hobbies:
            print(i)


# woman=Woman(25,"sila","ozyurt",65,"computer engineer",["basketball"])
# woman.introduce()
# woman.showAge()
# print(woman.calculateRestOfTheLife())
# woman.marryHuman()
# woman.marryHuman()
# woman.getAHobby("volleyball")
# woman.showHobbies()



