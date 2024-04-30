class example:
    def print(self):
        print("hello world")


class partyanimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("so far", self.x)


class abc:
    def __init__(self,a ,b):
        self.a=a
        self.b=b
    def sumof(self):
        print(self.a+self.b)


obj = abc(3,5)
obj.sumof()

eg = example()
eg.print()

an = partyanimal()
bn = partyanimal()
an.party()
an.party()
bn.party()
an.party()
