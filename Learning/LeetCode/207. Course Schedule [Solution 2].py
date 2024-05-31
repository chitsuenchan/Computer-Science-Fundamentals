





def canFinish(numCourses, prerequisites):

    # Map each course to prereq list
    # Populating the adjacency list
    #   Each i course mapped with a list of prerequities
    adj = {}
    for i in range(numCourses):
        adj[i] = []
    for a, b in prerequisites:
        adj[a].append(b)

    # below for Course Schedule II
    # res = []

    # detect a cycle
    cycle = set()
    # visit set all courses along the current DFS path
    seen = set()

    def dfs(current_node):
        if current_node in cycle:
            return False
        if current_node in seen:
            return True
        cycle.add(current_node)

        for child in adj[current_node]:
            if not dfs(child):
                return False
        cycle.remove(current_node)
        seen.add(current_node)

        # below for Course Schedule II
        # res.append(current_node)
        return True


    for i in range(numCourses):
        if not dfs(i):
            return False
            # return []
    return True
    # below for Course Schedule II
    # return res

# print(canFinish(2, [[1, 0], [0, 1]]))
# print(canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
print(canFinish(5, [[0,1],[0,2],[1,3],[1,4],[3,4]]))