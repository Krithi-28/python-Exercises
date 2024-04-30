class Heap:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.size=0
        self.heap=[0]*self.maxsize
        self.front=1
    def insert(self,data):
        if self.size <self.maxsize:
            self.heap[self.size]=data
            current=self.size
            self.size+=1
            while current >0:
                parent=(current-1)//2
                if self.heap[parent]<self.heap[current]:
                    self.heap[parent],self.heap[current]=self.heap[current],self.heap[parent]
                current=parent
    def print(self):
        print(self.heap)

a=Heap(9)
a.insert(3)
a.insert(2)
a.insert(5)
a.insert(4)
a.insert(10)
a.print()

