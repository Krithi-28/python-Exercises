class Graph:
    def __init__(self):
        self.graph={}
    def addvertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def addedges(self,vertex1,vertex2,isdirected=False):
        if vertex1 not in self.graph:
            self.addvertex(vertex1)
        if vertex2 not in self.graph:
            self.addvertex(vertex2)
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            if not isdirected:
                self.graph[vertex2].append(vertex1)
    def vertice(self):
        s=[]
        count=0
        for i in self.graph:
            s.append(i)
        for i in s:
            n=self.bfs(i)
            if len(n)==len(s):
                print(i)
        print(-1)


    def bfs(self,start):
        visited={start}
        p=[]
        stack=[start]
        while len(stack)>0:
            current=stack.pop(0)
            p.append(current)
            for child in self.graph[current]:
                if child not in visited:
                    stack.append(child)
                    visited.add(child)
        return p
g=Graph()
n=int(input("enter no of edges:"))
for i in range(n):
    a=input().split()
    g.addedges(a[0],a[1],True)
g.vertice()
