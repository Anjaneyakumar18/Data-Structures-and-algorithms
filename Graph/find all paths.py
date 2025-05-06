def findAllPaths(graph:dict[str:list],start,dest):
    ans=[]
    def dfs(start,destination,comb):
        if start==destination:
            ans.append(comb[:])
            return
        for node in graph[start]:
            dfs(node,destination,comb+[node])
    
    dfs(start,dest,[start])
    return ans
graph={
    'A':['B','C','D'],
    'B':['C','E'],
    'C':['D'],
    'D':['E'],
    'E':[]
}

ans=findAllPaths(graph,'A','E')
for path in ans:
    print("->".join(path))
    
