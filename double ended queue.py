class dequeue:
    def __init__(self):
        self.queue=[]
        self.front = -1
        self.rear = -1

    def isempty(self):
        if self.front == -1:
            return True
        else:
            return False
    def isfull(self,a):
        n=len(self.queue)
        if n==a:
            return True
        else:
            return False
    def insertatbeg(self,data,a):
        if self.isfull(a):
            print("overflow")
        else:
            if self.front==-1:
                self.queue.insert(0,data)
                self.front=0
                self.rear=0
            else:
                self.queue.insert(0,data)
                self.rear+=1
    def deleteatbeg(self):
        if self.isempty():
            print("underflow")
        else:
            del(self.queue[self.front])
    def display(self):
        print(self.queue)
    def insertatend(self,data,a):
        if self.isfull(a):
            print("overflow")
        else:
            self.queue.append(data)
            self.rear+=1
        self.display()
    def deleteatend(self):
        if self.isempty():
            print("underflow")
        else:
            del(self.queue[self.rear-1])
            self.rear-=1
        self.display()


de=dequeue()
a = int(input("enter no of data:"))
de.insertatbeg(1,a)
de.insertatbeg(2,a)
de.display()
de.insertatend(3,a)
de.deleteatbeg()
de.deleteatend()


