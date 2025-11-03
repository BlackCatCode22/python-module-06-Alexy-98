#New Class Extension, Subclassing
#Reuses exsisting class for a new one
class PartyAnimal:
    def __init__(self, nam):
        self.x = 0
        self.name = nam
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):
    #FootballFan is a class which extends to PartyAnimal
    #Has all the capabilities of PartyAnimal and more
    def __init__(self, nam):
        super().__init__(nam)
        self.points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,"points",self.points)