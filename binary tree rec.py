class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class binarytree:
    def __init__(self):
        self.root=None
    def add(self,data):
        if self.root is None:
            self.root=node(data)
            return
        self.recursiveadd(data,self.root)
    def recursiveadd(self,data,nodedata):
        if nodedata.left is None:
            nodedata.left=node(data)
        elif nodedata.right is None:
            nodedata.right=node(data)
        else:
            self.recursiveadd(data,nodedata.left)
    def print(self):
        print("\nPREORDER")
        self.preorder(self.root)
        print("\nINORDER")
        self.inorder(self.root)
        print("\nPOSTORDER")
        self.postorder(self.root)

    def preorder(self, nodedata):
        if nodedata is not None:
            print(nodedata.data, end=' ')
            self.preorder(nodedata.left)
            self.preorder(nodedata.right)

    def inorder(self, nodedata):
        if nodedata is not None:
            self.inorder(nodedata.left)
            print(nodedata.data, end=' ')
            self.inorder(nodedata.right)

    def postorder(self, nodedata):
        if nodedata is not None:
            self.inorder(nodedata.left)
            self.inorder(nodedata.right)
            print(nodedata.data, end=' ')
    def remove(self,data):
        if self.root is None:
            print("Binary tree is empty")
        else:
            if data==self.root.data:
                self.root=None
                return
            self.recursiveremove(data,self.root)
    def recursiveremove(self,data,nodedata):
        if nodedata.left.data==data:
            nodedata.left=None
            return
        elif nodedata.right.data==data:
            nodedata.right=None
            return
        elif nodedata.left:
            self.recursiveremove(data,nodedata.left)
        elif nodedata.right:
            self.recursiveremove(data,nodedata.right)
    def search(self,data):
        if self.root is None:
            print("Binary tree empty")
        else:
            if data==self.root.data:
                print("True")
                return
            self.recursivesearch(data,self.root)
    def recursivesearch(self,data,nodedata):
        if nodedata.data==data:
            print("True")
            return
        elif nodedata.left:
            self.recursivesearch(data,nodedata.left)
        elif nodedata.right:
            self.recursivesearch(data,nodedata.right)

bt=binarytree()
while True:
    print(
        "\nEnter your choice:\n1.INSERT NODE\n2.DISPLAY\n3.REMOVE NODE\n4.SEARCH\n5.EXIT")
    ch = int(input("Enter here:"))
    if ch==1:
        n = int(input("Enter the no of nodes:"))
        for i in range(n):
            data = int(input())
            bt.add(data)
    if ch==2:
        bt.print()
    if ch==3:
        data=int(input("Enter data to remove:"))
        bt.remove(data)
    if ch==4:
        s=int(input("Enter data to search:"))
        bt.search(s)
    if ch==5:
        exit()