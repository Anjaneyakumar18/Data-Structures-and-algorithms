def bfs(graph,start):
    visited=set([start])
    queue=[start]
    while queue:
        node=queue.pop(0)
        print(node)
        for neg in graph[node]:
            if neg not in visited:
                visited.add(neg)
                queue.append(neg)

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph,'A')
