class hashmap:
    def __init__(self):
        self.size=5
        self.dic=[None] * self.size
    def gethash(self,key):
        return hash(key)%self.size
    def insert(self,key,value):
        index=self.gethash(key)
        keyvalue=[key,value]
        if self.dic[index] is None:
            self.dic[index]=[keyvalue]
        else:
            for pair in self.dic[index]:
                if pair[0]==key:
                    pair[1]=value
                    break
            else:
                self.dic[index].append(keyvalue)
    def delete(self,key):
        index=self.gethash(key)
        if self.dic[index] is not None:
            for j,i in enumerate(self.dic[index]):
                if i[0]==key:
                    del self.dic[index][j]
                    break
    def getvalues(self,key):
        index=self.gethash(key)
        if self.dic[index] is not None:
            for i in self.dic[index]:
                if i[0]==key:
                    return i[1]
        return None
    def display(self):
        for items in self.dic:
            if items is not None:
                print(items)

h=hashmap()
print(h.dic)
h.insert("apple", 10)
h.insert("banana", 20)
h.insert("orange", 30)
h.insert("apple", 25)  # Update value for existing key
h.display()  # Display hash map
print(h.getvalues("banana"))  # Get value for key "banana"
h.delete("orange")
h.display()
