class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def create(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            newnode.prev=self.temp
            self.temp=newnode
            self.temp.next=None
    def print(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next
    def deletehead(self):
        self.temp=self.head
        self.head=self.head.next
        self.head.prev=None
        del(self.temp)
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
            self.pre=self.temp
            self.temp=self.temp.next
        self.pre.next=self.temp.next
        self.temp.next.prev=self.temp.prev
        del(self.temp)

    def insertatbeg(self,data):
        newdata=node(data)
        self.temp=self.head
        self.temp=newdata
        self.temp.next=self.head
        self.head.prev=newdata
        self.head=self.temp

    def insertatend(self,data):
        newdata=node(data)
        self.temp=self.head
        while self.temp.next:
            self.temp=self.temp.next
        self.temp.next=newdata
        newdata.prev=self.temp
        self.temp=newdata
        self.temp.next=None

    def insertatmid(self,data,pos):
        count=1
        self.temp=self.head
        newdata=node(data)
        while self.temp.next:
            self.temp=self.temp.next
            count+=1
            if count==pos-1:
                newdata.next=self.temp.next
                newdata.next.prev=newdata
                newdata.prev=self.temp
                self.temp.next=newdata
doublylinkedlist=dll()
while True:
    print("\nEnter your choice:\n1.Create\n2.Display\n3.delete head\n4.delete end\n5.delete at mid\n6.Insert at beg\n7.Insert at end\n8.Insert at mid\n9.Exit")
    choice=int(input("enter here:"))
    if choice==1:
        a = int(input("enter no of data:"))
        for i in range(a):
            data = int(input("enter data:"))
            doublylinkedlist.create(data)
    if choice==2:
        doublylinkedlist.print()
    if choice==3:
        doublylinkedlist.deletehead()
    if choice==4:
        doublylinkedlist.deleteend()
    if choice==5:
        doublylinkedlist.deletemid()
    if choice==6:
        new = int(input("enter element to insert at beg:"))
        doublylinkedlist.insertatbeg(new)
    if choice==7:
        new = int(input("enter element to insert at end: "))
        doublylinkedlist.insertatend(new)
    if choice==8:
        new = int(input("enter element to insert at mid:"))
        pos = int(input("enter index to insert:"))
        doublylinkedlist.insertatmid(new, pos)
    if choice==9:
        exit()