class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublycircular:
    def __init__(self):
        self.head=None
        self.temp=None
        self.last=None
    def create(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.temp=newnode
            self.last=newnode

        else:
            self.temp.next=newnode
            self.head.prev=newnode
            newnode.prev=self.temp
            self.temp=newnode
            self.last=newnode
    def print(self):
        self.temp=self.head
        while (self.temp!=self.last):
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
        print(self.last.data)
    def deletehead(self):
        self.temp=self.head
        self.head=self.head.next
        self.head.prev=self.last
        self.last.next=self.head
        del(self.temp)
        print(self.last.next.data)
        print(self.head.prev.data)
    def deleteend(self):
        self.temp=self.last
        self.last=self.last.prev
        self.head.prev=self.last
        self.last.next=self.head
        print(self.last.next.data)
        print(self.head.prev.data)
    def deletemid(self):
        ele = int(input("enter element to delete:"))
        self.temp = self.head
        while self.temp.next:
            if self.temp.data == ele:
                break
            prev = self.temp
            self.temp = self.temp.next
        prev.next = self.temp.next
        del (self.temp)
    def insertatbeg(self,data):
        newdata=node(data)
        self.temp=newdata
        self.last.next=newdata
        self.head.prev=newdata
        newdata.next=self.head
        newdata.prev=self.last
        self.head=newdata
        print(self.head.data)
        print(self.last.next.data)
        print(self.head.next.data)
    def insertatend(self,data):
        newdata=node(data)
        self.temp=newdata
        newdata.prev=self.last
        newdata.next=self.head
        self.last.next=newdata
        self.head.prev=newdata
        self.last=newdata
        print(self.last.data)
        print(self.head.prev.data)
        print(self.last.next.data)
    def insertatmid(self,data,pos):
        count=1
        self.temp=self.head
        newdata=node(data)
        while count < pos-1:
            self.temp = self.temp.next
            count += 1
        newdata.next=self.temp.next
        self.temp.next=newdata

dc=doublycircular()
while True:
    print("\nEnter your choice:\n1.Create\n2.Delete head\n3.Delete end\n4.Delete at mid\n5.Insert at beg\n6.Insert at end\n7.Insert at mid\n8.Display\n9.exit")
    choice=int(input("enter here:"))
    if choice==1:
        a = int(input("enter no of data:"))
        for i in range(a):
            data = int(input("enter data:"))
            dc.create(data)
    if choice==2:
        dc.deletehead()
    if choice==3:
        dc.deleteend()
    if choice==4:
        dc.deletemid()
    if choice==5:
        new=int(input("enter element to insert at beg:"))
        dc.insertatbeg(new)
    if choice==6:
        new=int(input("enter element to insert at end: "))
        dc.insertatend(new)
    if choice==7:
        new=int(input("enter element to insert at mid:"))
        pos=int(input("enter index to insert:"))
        dc.insertatmid(new,pos)
    if choice==8:
        dc.print()
    if choice==9:
        exit()
