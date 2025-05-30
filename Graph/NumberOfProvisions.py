# Leetcode 547
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph={}
        for i in range(len(isConnected)):
            graph[i]=[]
            for j in range(len(isConnected[0])):
                if i==j:
                    continue
                if isConnected[i][j]!=0:
                    graph[i].append(j)
        
        seen=set()
        pro=0
        def populateSeen(start):
            if start in seen:
                return
            seen.add(start)
            for node in graph[start]:
                populateSeen(node)
        
        for node,lst in graph.items():
            if node not in seen:
                pro+=1
                populateSeen(node)
        return pro

                
