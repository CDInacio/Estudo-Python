def depth_first_search_iterative(graph, node):
    visited = set()
    if node not in graph:
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)


graph1 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'D'],
    'C': ['A', 'D'],
    'D': ['A', 'B', 'C', 'D', 'E'],
    'E': ['B', 'D']
}

depth_first_search_iterative(graph1, 'A')
