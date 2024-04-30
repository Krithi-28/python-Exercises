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
    def swap(self,n):
        count=1
        while self.temp:
            count+=1
            self.temp=self.temp.next
            if count%2==0 and n%2==0:
                first=self.temp
                lst=self.last
                if lst.next is None:
                    self.lst.next=first.next
                    first.next=None
                else:
                    nxt=lst.next
                    self.lst.next=first.next


ll=linkedlist()
n=int(input("enter no of datas:"))
for i in range(n):
    data= int(input("enter data:"))
    ll.create(data)
ll.display()