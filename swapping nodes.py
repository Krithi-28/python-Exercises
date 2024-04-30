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
    def display(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
    def swap(self,a,b):
        self.temp=self.head
        while self.temp:
            if self.temp.data==a:
                temp1=self.temp
                break
            prev1=self.temp
            self.temp=self.temp.next
        print("temp1 address:",temp1)
        self.temp=self.head
        while self.temp:
            if self.temp.data==b:
                temp2=self.temp
                break
            prev2=self.temp
            self.temp=self.temp.next
        print("temp2 address:",temp2)
        if temp1==self.head:
            self.head=temp2
            prev2.next = temp1
            next2 = temp2.next
            next1 = temp1.next
            temp1.next = next2
            self.head.next = next1
        elif temp2==self.head:
            self.head=temp1
            prev1.next = temp2
            next2 = temp2.next
            next1 = self.head.next
            self.head.next = next2
            temp2.next = next1
        else:
            prev1.next = temp2
            prev2.next = temp1
            next2 = temp2.next
            next1 = temp1.next
            temp1.next = next2
            temp2.next = next1
        print("temp1 address",temp1)
        print("temp2 address",temp2)





ll=linkedlist()
n=int(input("enter no of datas:"))
for i in range(n):
    data= int(input("enter data:"))
    ll.create(data)
ll.display()
a=int(input("\nenter first number to swap:"))
b=int(input("\nenter second number to swap:"))
ll.swap(a,b)
ll.display()