class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublydequeue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.temp=None

    def isempty(self):
        if self.front == None:
            return True
        else:
            return False
    def insertatbeg(self,data):
        newnode=node(data)
        if self.front is None:
            self.front=newnode
            self.rear=newnode
        else:
            self.front.prev=newnode
            newnode.next=self.front
            self.front=newnode
    def insertatend(self,data):
        newnode=node(data)
        if self.rear==None:
            self.rear=newnode
            self.front=newnode
        else:
            self.rear.next=newnode
            newnode.prev=self.rear
            self.rear=newnode
    def deleteatbeg(self):
        self.temp = self.front
        if self.isempty():
            print("Underflow")
        else:
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                del (self.temp)
                self.front = self.front.next
                self.front.prev=None
    def deleteatend(self):
        self.temp = self.rear
        if self.isempty():
            print("Underflow")
        else:
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                del (self.temp)
                self.rear=self.rear.prev
                self.rear.next=None
    def display(self):
        self.temp=self.front
        if self.isempty():
            print("Underflow")
        else:
            while self.temp:
                print(self.temp.data, end=' ')
                self.temp = self.temp.next
de=doublydequeue()
while True:
    print(
        "\nEnter your choice:\n1.insertatbeg\n2.insertatend\n3.deleteatbeg\n4.deleteatend\n5.display\n6.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        data=int(input())
        de.insertatbeg(data)
    if choice==2:
        data=int(input())
        de.insertatend(data)
    if choice==3:
        de.deleteatbeg()
    if choice==4:
        de.deleteatend()
    if choice==5:
        de.display()
    if choice==6:
        exit()