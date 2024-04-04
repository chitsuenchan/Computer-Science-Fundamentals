from collections import deque

def bfs(n, m, edges, s):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    distance = [-1] * (n + 1)

    queue = deque()
    queue.append(s)
    visited[s] = True
    distance[s] = 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 6
                queue.append(neighbor)

    return distance[1:s] + distance[s + 1:]