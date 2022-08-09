def breadth_first_search(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        for neighbour in graph(s):
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)


adjacency_list = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

breadth_first_search(adjacency_list, 'A')
