import heapq
class Graph:
    def __init__(self):
        self.graph={}
    def addvertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def addedges(self,vertex1,vertex2,weight):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append((vertex2,weight))
            self.graph[vertex2].append((vertex1, weight))
    def display(self):
        for key,value in self.graph.items():
            print(f"{key}==>{value}")
    def shortestdistance(self,start):
        distance={node:float('inf') for node in self.graph}
        distance[start]=0
        minheap=[(0,start)]
        while minheap:
            dist,curr=heapq.heappop(minheap)
            if dist >distance[curr]:
                continue
            for neighbor,weight in self.graph[curr]:
                path = dist + weight
                if path<distance[neighbor]:
                    distance[neighbor]=path
                    heapq.heappush(minheap,(path,neighbor))
        return distance

g=Graph()
while True:
    print(
        "\nEnter your choice:\n1.ADD VERTEX\n2.ADD EDGES\n4.DIJIKSTRA\n5.EXIT")
    ch=int(input("Enter here:"))
    if ch==1:
        n=int(input("Enter the no of vertices:"))
        for i in range(n):
            vertex=input()
            g.addvertex(vertex)
    if ch==2:
        n=int(input("Enter no of edges:"))
        for i in range(n):
            vertex1=input("enter vertex1:")
            vertex2=input("enter vertex2:")
            weight=int(input("enter weight of the edge:"))
            g.addedges(vertex1,vertex2,weight)

            # edge=input(f"enter edge {i+1}(vertex1 vertex2):").split()
            # if len(edge)==2:
            #     g.addedge(edge[0],edge[1])
            # else:
            #     print("Invalid input. Please enter two vertices for an edge.")
    if ch==3:
        g.display()
    if ch==4:
        start=input()
        dijikstra=g.shortestdistance(start)
        for node,distance in dijikstra.items():
            print((node,distance))
    if ch==5:
        exit()