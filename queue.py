class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def isempty(self):
        if self.front==None:
            return True
        else:
            return False
    def enqueue(self,data):
        newnode=node(data)
        if self.front==None:
            self.front=newnode
            self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
    def dequeue(self):
        temp=self.front
        if self.isempty():
            print("queue is empty")
        else:
            self.front=self.front.next
            del(temp)
    def display(self):
        temp=self.front
        if self.isempty():
            print("queue is empty")
        else:
            while temp:
                print(temp.data,end=' ')
                temp=temp.next
q=queue()
while True:
    print(
        "\nEnter your choice:\n1.ENQUEUE\n2.DEQUEUE\n3.DISPLAY\n4.EXIT")
    choice = int(input("enter here:"))
    if choice == 1:
        a = int(input("enter no of data:"))
        for i in range(a):
            data = int(input("enter data:"))
            q.enqueue(data)
    if choice==2:
        q.dequeue()
    if choice==3:
        q.display()
    if choice==4:
        exit()