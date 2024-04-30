class graph:
    def __init__(self,size):
        self.adj=[]
        for i in range(size):
            self.adj.append([0 for i in range(size)])
        self.size=size
    def addedge(self,v1,v2):
        self.adj[v1][v2]=1
        self.adj[v2][v1]=1
    def display(self):
        print(self.adj)
n=int(input("enter no of nodes:"))
g=graph(n)
g.addedge(1,2)
g.addedge(1,4)
g.display()


