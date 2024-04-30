class cqueue:
    def __init__(self,a):
        self.a=a
        self.queue=[None for i in range(a)]
        self.front=-1
        self.rear=-1
    def isfull(self,a):

        if ((self.rear+1)%a==self.front):
            return True
        else:
            return False

    def isempty(self):
        if self.front == -1 and self.rear==-1:
            return True
        else:
            return False
    def enqueue(self,data,a):
        if self.isfull(a):
            print("overflow")
        elif self.rear==-1:
                self.rear=0
                self.front=0
                self.queue[self.rear]=data
        else:
                self.rear=(self.rear+1)%a
                self.queue[self.rear]=data
    def dequeue(self,a):
        if self.isempty():
            print("underflow")
        else:
            self.front=(self.front+1)%a
            del(self.queue[self.front])
    def display(self,a):
        i=0
        while self.queue[i] and i<a:
            print(self.queue[i])
            i+=1
a=int(input())
cq=cqueue(a)
while True:
    print(
        "\nEnter your choice:\n1.enqueue\n2.dequeue\n3.display\n4.exit")
    choice = int(input("enter your choice:"))
    if choice==1:
        data=int(input())
        cq.enqueue(data,a)
    if choice==2:
        cq.dequeue(a)
    if choice==3:
        cq.display(a)
    if choice==4:
        exit()


