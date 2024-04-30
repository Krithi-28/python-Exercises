class dog:
    type="pug"
    def nameofdog(self,name):
        print(name)
o1=dog()
o2=dog()
o1.nameofdog("scooby")
print(o1.type,o2.type)
o2.nameofdog("chocolate")
# class dog:
#     type="pug"
#     def __init__(self,name):
#         self.name=name
#     def nameofdog(self):
#         print(self.name)
# o1=dog("scooby")
# o2=dog("chocolate")
# o1.nameofdog()
# print(o1.type,o2.type)
# o2.nameofdog()
