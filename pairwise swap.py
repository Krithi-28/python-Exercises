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
            self.last=newnode

    def display(self):
        self.temp = self.head
        while self.temp:
            print(self.temp.data, end=' ')
            self.temp = self.temp.next
    def pairswap(self):
        self.temp=self.head
        nxt=self.head.next
        self.head=self.temp
        self.
ll=linkedlist()
n=int(input("enter no of datas:"))
for i in range(n):
    data= int(input("enter data:"))
    ll.create(data)
ll.display()