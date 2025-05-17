def dfs(graph,start):
    visited=set([start])
    stack=[start]
    while stack:
        print(stack[-1])
        for neg in graph[stack.pop()]:
            if neg not in visited:
                visited.add(neg)
                stack.append(neg)

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph,'A')
