class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=newnode
    def print(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
    def sort(self):
        swapped=True
        while swapped:
            swapped=False
            self.temp = self.head
            while self.temp.next:
                if self.temp.data > self.temp.next.data:
                    t=self.temp.next.data
                    self.temp.next.data=self.temp.data
                    self.temp.data=t
                    swapped=True
                self.temp=self.temp.next
ll=linkedlist()
n=int(input("enter no of datas:"))
for i in range(n):
    data= int(input("enter data:"))
    ll.create(data)
ll.print()
ll.sort()
print()
ll.print()
