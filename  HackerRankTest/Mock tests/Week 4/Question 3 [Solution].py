def cutTheTree(data, edges):
    n = len(data)

    # Calculate the total sum of the tree
    total_sum = sum(data)

    # Create an adjacency list representation of the tree
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u - 1].append(v - 1)
        adj_list[v - 1].append(u - 1)

    min_diff = float('inf')
    visited = [False] * n

    # Function to perform post-order traversal and calculate subtree sums
    def dfs(root):
        nonlocal min_diff
        stack = [(root, -1)]
        subtree_sums = [0] * n

        while stack:
            node, parent = stack.pop()
            if node >= 0:
                if visited[node]:
                    subtree_sums[node] = data[node]
                    for neighbor in adj_list[node]:
                        if neighbor != parent:
                            subtree_sums[node] += subtree_sums[neighbor]
                    min_diff = min(min_diff, abs(total_sum - 2 * subtree_sums[node]))
                else:
                    visited[node] = True
                    stack.append((node, parent))
                    for neighbor in adj_list[node]:
                        if neighbor != parent:
                            stack.append((neighbor, node))
            else:
                node = ~node
                subtree_sums[node] = data[node]
                for neighbor in adj_list[node]:
                    if neighbor != parent:
                        subtree_sums[node] += subtree_sums[neighbor]
                min_diff = min(min_diff, abs(total_sum - 2 * subtree_sums[node]))

        return subtree_sums[root]

    # Start DFS from node 0 (root)
    dfs(0)

    return min_diff

data = [1, 2, 3, 4, 5, 6, 7]
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
# Expected Output: 1



data = [5, 5, 5, 5, 5, 5, 5]
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
# Expected Output: 0

data = [10, 20, 30, 40, 50, 60, 70]
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
# Expected Output: 20
