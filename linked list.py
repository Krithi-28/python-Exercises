class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    def create(self,data):
        newnode=node(data)
        if (self.head is None):
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=self.temp.next

    def print(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
    def deletehead(self):
        self.temp=self.head
        self.head=self.head.next
        self.temp=self.head
    def deleteend(self):
        self.temp=self.head
        while self.temp.next:
            self.prev=self.temp
            self.temp=self.temp.next
        self.prev.next=None
        del(self.temp)
    def deletemid(self):
        ele=int(input("enter element to delete:"))
        self.temp=self.head
        while self.temp.next:
            if self.temp.data==ele:
                break
            self.prev=self.temp
            self.temp=self.temp.next
        self.prev.next=self.temp.next
        del(self.temp)

    def insertatbeg(self,data):
        self.newdata=node(data)
        self.temp=self.head
        self.temp=self.newdata
        self.temp.next=self.head
        self.head=self.temp
    def insertatend(self,data):
        newdata=node(data)
        self.temp=self.head
        while self.temp.next:
            self.temp=self.temp.next
        self.temp.next=newdata
        self.temp=newdata
        self.temp.next=None
    def insertatmid(self,data,pos):
        count=1
        self.temp=self.head
        newdata=node(data)
        while self.temp.next:
            self.temp=self.temp.next
            count+=1
            if count==pos:
                newdata.next=self.temp.next
                self.temp.next=newdata









linkedlist=ll()
while True:
    print("\nEnter your choice:\n1.Create\n2.Delete head\n3.Delete end\n4.Delete at mid\n5.Insert at beg\n6.Insert at end\n7.Insert at mid\n8.Display\n9.exit")
    choice=int(input("enter here:"))
    if choice==1:
        a = int(input("enter no of data:"))
        for i in range(a):
            data = int(input("enter data:"))
            linkedlist.create(data)
    if choice==2:
        linkedlist.deletehead()
    if choice==3:
        linkedlist.deleteend()
    if choice==4:
        linkedlist.deletemid()
    if choice==5:
        new=int(input("enter element to insert at beg:"))
        linkedlist.insertatbeg(new)
    if choice==6:
        new=int(input("enter element to insert at end: "))
        linkedlist.insertatend(new)
    if choice==7:
        new=int(input("enter element to insert at mid:"))
        pos=int(input("enter index to insert:"))
        linkedlist.insertatmid(new,pos)
    if choice==8:
        linkedlist.print()
    if choice==9:
        exit()

