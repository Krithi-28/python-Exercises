class Graph:
    def __init__(self):
        self.graph={}
    def addvertex(self,vertex):
        self.graph[vertex]=[]
    def addedges(self,vertex1,vertex2,isdirected=False):
        if vertex1 not in self.graph:
            self.addvertex(vertex1)
        if vertex2 not in self.graph:
            self.addvertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if not isdirected:
            self.graph[vertex2].append(vertex1)
    def cyclic(self):
        visited=set()
        stack=set()
        def dfs(node):
            visited.add(node)
            stack.add(node)
            for child in self.graph:
                if child not in visited:
                    if dfs(child):
                        return True
                    elif child in stack:
                        return False
            stack.remove(node)
            return False
        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex):
                    return True
        return False
g=Graph()
n=int(input("enter no of edges:"))
for i in range(n):
    a=input().split()
    g.addedges(a[0],a[1],True)
if g.cyclic():
    print("cyclic")
else:
    print("not cyclic")
