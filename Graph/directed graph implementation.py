class graph:
    def __init__(self):
        self.graph={}

    def addnode(self,node):
        if node not in self.graph:
            self.graph[node]=[]
    
    def add_all_edges(self,node1,*nodes):
        for node in nodes:
            if node not in self.graph:
                self.graph[node]=[]
        self.graph[node1].extend(list(nodes))

    def view(self):
        for key in self.graph.keys():
            print(f'{key} : {self.graph[key]}')

g=graph()
g.addnode('A')
g.addnode('B')
g.addnode('C')
g.add_all_edges('A','B','C')
g.add_all_edges('B','C')
g.view()

# this is undirected graph implementation
'''
        
          A
         / \
        /   \
       V     V
       B---->C

'''