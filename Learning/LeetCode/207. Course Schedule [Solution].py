def canFinish(numCourses, prerequisites):
    # Map each course to prereq list
    graph = {i: [] for i in range(numCourses)}

    # Populating the preMap dictionary
    #   Each course mapped with a list of prerequities (making an adjacency hashmap)
    for course, prerequisite in prerequisites:
        graph[course].append(prerequisite)

    # visit set all courses along the current DFS path
    visitSet = set()

    def dfs(course):
        if course in visitSet:
            return False
        if graph[course] == []:
            return True

        visitSet.add(course)
        for prerequisite in graph[course]:
            if not dfs(prerequisite):
                return False

        visitSet.remove(course)
        graph[course] = []
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False
    return True


# print(canFinish(2, [[1, 0], [0, 1]]))
# print(canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
print(canFinish(5, [[0,1],[0,2],[1,3],[1,4],[3,4]]))
