
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs(root, target):
    if not root:
        return

    if root.value == target:
        return True

    for child in root.children:
        if dfs(child, target):
            return True

    return False



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.children = [b,c]
b.children = [d,e]
c.children = [f]

print(dfs(a,"t"))