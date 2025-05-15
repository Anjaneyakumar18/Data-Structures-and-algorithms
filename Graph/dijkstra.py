import heapq


def dijkstra(graph,start,end):
    seen=set([start])
    min_heap=[]
    heapq.heappush(min_heap,(0,start,[start]))
    while min_heap:
        current_dist,start,path=heapq.heappop(min_heap)
        if start==end:
            return current_dist,path
        for n,dist in graph[start]:
            if n not in seen:
                heapq.heappush(min_heap,(current_dist+dist,n,path+[n]))
                seen.add(n)
    return -1,[]

graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('D', 1), ('E', 4)],
    'C': [('B', 2), ('F', 5)],
    'D': [('E', 1)],
    'E': [('G', 3)],
    'F': [('E', 2), ('G', 1)],
    'G': [('H', 2)],
    'H': [('I', 1)],
    'I': [('J', 2)],
    'J': []
}
   

print(dijkstra(graph,'A','J'))
