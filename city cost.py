class Graph:
    def __init__(self):
        self.graph={}
    def addvertex(self,vertex):
        self.graph[vertex]=[]
    def addedges(self,vertex1,vertex2,price,isdirected=True):
        if vertex1 not in self.graph:
            self.addvertex(vertex1)
        if vertex2 not in self.graph:
            self.addvertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex1].append(price)
    def display(self):
        for key, values in self.graph.items():
            print(f"{key}==>{values}")
    def shortestdistance(self,start,dest):
        visited={start}
        queue=[(start,[start])]
        while len(queue)>0:
            current,path=queue.pop(0)
            print(current)
g=Graph()
n=int(input("enter no of edges:"))
for i in range(n):
    a=input().split()
    p=int(input())
    g.addedges(a[0],a[1],p,True)
g.display()