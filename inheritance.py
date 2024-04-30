class partyanimal:
    x=0
    name=' '
    def __init__(self,name):
        self.name=name
        print(self.name,"constructed")
    def party(self):
        self.x=self.x+1
        print(self.name,"party count",self.x)
class cricket(partyanimal):
    points=0
    def six(self):
        self.points=self.points+6
        self.party()
        print(self.name,"points",self.points)
s=partyanimal("sally")
s.party()
j=cricket("jim")
j.party()
j.six()

