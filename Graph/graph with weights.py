class graph:
    def __init__(self):
        self.graph={}
    
    def add(self,source,dest,weight):
        if source not in self.graph:
            self.graph[source]=[(dest,weight)]
            return 
        self.graph[source].append((dest,weight))
        return
    
    def visit(self):
        for n in self.graph.keys():
            for o,d in self.graph[n]:
                print(n,'-',d,'->',o)

g=graph()
g.add('A','B',6)
g.add('A','C',11)
g.add('B','C',7)
g.add('C','D',8)

g.visit()

# A - 6 -> B
# A - 11 -> C
# B - 7 -> C
# C - 8 -> D
