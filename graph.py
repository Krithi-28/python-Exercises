class Graph:
    def __init__(self):
        self.graph={}
    def addvertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def addedge(self,vertex1,vertex2,isdirected=False):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            if not isdirected:
                self.graph[vertex2].append(vertex1)
    def display(self):
        for key,value in self.graph.items():
            print(f"{key}==>{value}")
    def printvertices(self):
        for i in self.graph:
            print(i,end=' ')
    def printedges(self):
        for key,value in self.graph.items():
            for vertex in value:
                print(f"{key},{vertex}")
    def removevertex(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for key,value in self.graph.items():
                if vertex in value:
                    value.remove(vertex)
    def removeedges(self,vertex1,vertex2):
        if vertex1 in self.graph[vertex2]:
            self.graph[vertex2].remove(vertex1)
        if vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)


    def dfstraversal(self,start,alreadyvisited=set()):
        if start not in alreadyvisited:
            alreadyvisited.add(start)
            print(start,end=' ')
            for child in self.graph[start]:
                self.dfstraversal(child,alreadyvisited)

    def bfstraversal(self,start):
        alreadyvisited={start}
        queue=[start]
        while len(queue)>0:
            current=queue.pop(0)
            print(current,end=' ')
            for child in self.graph[current]:
                if child not in alreadyvisited:
                    queue.append(child)
                    alreadyvisited.add(child)
    def shortestpath(self,start,end):
        alreadyvisited = {start}
        queue = [(start,[start])]
        while len(queue) > 0:
            current,path = queue.pop(0)
            for child in self.graph[current]:
                if child==end:
                    return path+[child]
                if child not in alreadyvisited:
                    queue.append((child,path+[child]))
                    alreadyvisited.add(child)

g=Graph()
while True:
    print(
        "\nEnter your choice:\n1.ADD VERTEX\n2.ADD EDGES\n3.REMOVE VERTEX\n4.REMOVE EDGES\n5.DISPLAY\n6.DISPLAY VERTICES\n7.DISPLAY EDGES\n8.DFS TRAVERSAL\n9.BFS TRAVERSAL\n0.SHORTEST PATH\n11.EXIT")
    ch=int(input("Enter here:"))
    if ch==1:
        n=int(input("Enter the no of vertices:"))
        for i in range(n):
            vertex=input()
            g.addvertex(vertex)
    if ch==2:
        n=int(input("Enter no of edges:"))
        for i in range(n):
            edge=input(f"enter edge {i+1}(vertex1 vertex2):").split()
            if len(edge)==2:
                g.addedge(edge[0],edge[1])
            else:
                print("Invalid input. Please enter two vertices for an edge.")
    if ch==3:
        vertex=input("enter vertex to remove:")
        g.removevertex(vertex)
    if ch==4:
        edge=input(f"enter edge{i+1}(vertex1 vertex2):").split()
        if len(edge)==2:
            g.removeedges(edge[0],edge[1])
    if ch==5:
        g.display()
    if ch==6:
        g.printvertices()
    if ch==7:
        g.printedges()
    if ch==8:
        start=input("Enter starting vertex to traverse:")
        g.dfstraversal(start)
    if ch==9:
        start=input("Enter starting vertex to traverse:")
        g.bfstraversal(start)
    if ch==0:
        start=input("Enter the starting vertex:")
        end=input("Enter the end vertex:")
        print(g.shortestpath(start,end))
    if ch==11:
        exit()


