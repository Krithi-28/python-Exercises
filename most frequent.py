class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.next = None
        self.head = None
        self.temp = None

    def create(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.temp = self.head
        else:
            self.temp.next = newnode
            self.temp = newnode

    def display(self):
        temp = self.head
        if self.head is None:
            print("None")
            return
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def divisible(self):
        temp = self.head
        f = {}
        while temp:
            if temp.data in f:
                f[temp.data] += 1
                temp = temp.next
            else:
                f[temp.data] = 1
                temp = temp.next
        b = list(f.keys())[list(f.values()).index(max(f.values()))]
        c = min(f.keys())
        if b%c == 0:
            return True
        else:
            return False


ll = LinkedList()
# a = [2,3,3,3,4,5]
a = list(map(int,input().split()))
for i in a:
    ll.create(i)
print(ll.divisible())