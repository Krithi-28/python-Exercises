class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.temp=None
        self.last=None
    def create(self,data):
        newnode=node(data)
        if (self.head is None):
            self.head=newnode
            self.temp=newnode
            self.last=newnode
        else:
            self.temp.next=newnode
            self.temp=self.temp.next
            self.last=newnode

    def print(self):
        self.temp = self.head
        if self.head is None:
            print("No elements in the linked list")
        else:
            while self.temp:
                print(self.temp.data, end=' ')
                self.temp = self.temp.next
    def deletenode(self,pos):
        if pos==1:
            self.head=None
        else:
            count=1
            self.temp=self.head
            while self.temp!=self.last:
                prev=self.temp
                self.temp=self.temp.next
                count+=1
                if count%pos==0:
                    if self.temp==self.head:
                        delete = self.temp
                        self.head=self.temp.next
                        del (delete)
                    elif self.temp==self.last:
                        delete=self.temp
                        prev.next=None
                    else:
                        delete = self.temp
                        prev.next = self.temp.next
                        del (delete)


ll=linkedlist()
n=int(input("enter no of datas:"))
for i in range(n):
    data= int(input("enter data:"))
    ll.create(data)
ll.print()
p=int(input("\nenter position to delete:"))
ll.deletenode(p)
ll.print()