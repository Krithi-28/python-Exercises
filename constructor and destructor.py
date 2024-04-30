class partyanimal:
    x=0
    def __init__(self):
        print("constructor")
    def party(self):
        self.x=self.x+1
        print("so far",self.x)
    def __del__(self):
        print("destructor",self.x)
an=partyanimal()
an.party()
# bn=partyanimal()
# bn.party()
an.party()
an.party()
# an="hello"
# print(an)