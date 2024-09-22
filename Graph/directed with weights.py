class Graph:
    def __init__(self):
        self.graph={}
    
    def addnode(self,node):
        if node not in self.graph:
            self.graph[node]=[]
    
    def addedges(self,node1,node2,distance):
        if node1 not in self.graph:
            self.graph[node1]=[]
        if node2 not in self.graph:
            self.graph[node2]=[]

        self.graph[node1].append((node2,distance))
        
    def view(self):
        for key in self.graph.keys():
            print(f'{key} : {self.graph[key]}')


g=Graph()
g.addedges('A','B',10)
g.addedges('A','C',20)
g.addedges('C','B',30)
g.view()