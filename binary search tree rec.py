class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class binarysearchtree:
    def __init__(self):
        self.root=None
    def add(self,data):
        if self.root is None:
            self.root=node(data)
            return
        self.insert(data,self.root)
    def insert(self,data,newnode):
        if data<newnode.data:
            if newnode.left is None:
                newnode.left = node(data)
            else:
                 self.insert(data, newnode.left)
        elif data>=newnode.data:
            if newnode.right is None:
                newnode.right=node(data)
            else:
                self.insert(data,newnode.right)
    def print(self):
        print("\nPREORDER")
        self.preorder(self.root)
        print("\nINORDER")
        self.inorder(self.root)
        print("\nPOSTORDER")
        self.postorder(self.root)
    def preorder(self,nodedata):
        if nodedata is not None:
            print(nodedata.data,end=' ')
            self.preorder(nodedata.left)
            self.preorder(nodedata.right)
    def inorder(self,nodedata):
        if nodedata is not None:
            self.inorder(nodedata.left)
            print(nodedata.data, end=' ')
            self.inorder(nodedata.right)
    def postorder(self,nodedata):
        if nodedata is not None:
            self.inorder(nodedata.left)
            self.inorder(nodedata.right)
            print(nodedata.data, end=' ')
    def remove(self,data):
        self.removes(data,self.root)
    def removes(self,data,nodedata):
        if nodedata is None:
            return nodedata
        if nodedata.data>data:
            nodedata.left=self.removes(data,nodedata.left)
            return nodedata
        elif nodedata.data<data:
            nodedata.right=self.removes(data,nodedata.right)
            return nodedata
        if nodedata.left is None:
            temp=nodedata.right
            del nodedata
            return temp
        elif nodedata.right is None:
            temp=nodedata.left
            del nodedata
            return temp
        else:
            succparent=nodedata
            succ=nodedata.right
            while succ.left is not None:
                succparent=succ
                succ=succ.left
            if succparent!=nodedata:
                succparent.left=succ.right
            else:
                succparent.right=succ.right
            nodedata.data=succ.data
            del succ
            return nodedata
    def search(self,s):
        find=self.recursivesearch(s,self.root)
        if find:
            print("TRUE")
        else:
            print("FALSE")
    def recursivesearch(self,s,nodedata):
        if nodedata is None or nodedata.data==s:
            return nodedata
        elif s <  nodedata.data:
            return self.recursivesearch(s,nodedata.left)
        elif s > nodedata.data:
            return self.recursivesearch(s,nodedata.right)
bst=binarysearchtree()
while True:
    print(
        "\nEnter your choice:\n1.INSERT NODE\n2.DISPLAY\n3.REMOVE NODE\n4.SEARCH\n5.EXIT")
    ch = int(input("Enter here:"))
    if ch==1:
        n = int(input("Enter the no of nodes:"))
        for i in range(n):
            data = int(input())
            bst.add(data)
    if ch==2:
        bst.print()
    if ch==3:
        data=int(input("Enter data to remove:"))
        bst.remove(data)
    if ch==4:
        s=int(input("Enter data to search:"))
        bst.search(s)
    if ch==5:
        exit()