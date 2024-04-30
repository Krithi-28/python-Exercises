class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
        self.temp=None
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def push(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def display(self):
        self.temp=self.head
        if self.isempty():
            print("underflow")
        else:
            while self.temp:
                print(self.temp.data,end=' ')
                self.temp=self.temp.next
    def pop(self):
        self.temp=self.head
        if self.isempty():
            print("underflow")
        else:
            self.head=self.head.next
            del(self.temp)
    def peek(self):
        if self.isempty():
            print("underflow")
        else:
            print(self.head.data)


s=stack()
while True:
    print(
        "\nEnter your choice:\n1.PUSH\n2.POP\n3.PEEK\n4.DISPLAY\n5.EXIT")
    choice = int(input("enter here:"))
    if choice == 1:
        a = int(input("enter no of data:"))
        for i in range(a):
            data = int(input("enter data:"))
            s.push(data)
    if choice==2:
        s.pop()
    if choice==3:
        s.peek()
    if choice==4:
        s.display()
    if choice==5:
        exit()