def componentsInGraph(bg):
    # Create adjacency list representation of the graph
    adj_list = [[] for _ in range(2 * len(bg) + 1)]
    for edge in bg:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    # Function to perform depth-first search
    def dfs(start_node, visited):
        stack = [start_node]
        size = 0
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                size += 1
                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return size

    min_size = float('inf')
    max_size = 0
    visited = set()
    for i in range(1, len(adj_list)):
        if i not in visited:
            component_size = dfs(i, visited)
            # Ignore single nodes
            if component_size > 1:
                min_size = min(min_size, component_size)
                max_size = max(max_size, component_size)

    return [min_size, max_size]

bg = [(1, 2), (2, 3), (3, 4)]
print(componentsInGraph(bg))  # Expected output: [4, 4]

bg = [(1, 2), (3, 4)]
print(componentsInGraph(bg))  # Expected output: [2, 2]

bg = [(1, 2), (3, 4), (5, 6)]
print(componentsInGraph(bg))  # Expected output: [2, 2]


