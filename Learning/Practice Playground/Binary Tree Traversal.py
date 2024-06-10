class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# pre-order traversal

def pre_order(root, lst = []):

    if root:
        lst.append(root.val)
        pre_order(root.left)
        pre_order(root.right)

    return lst

# in-order traversal
def in_order(root, lst = []):

    if root:
        in_order(root.left)
        lst.append(root.val)
        in_order(root.right)

    return lst

# post-order traversal
def post_order(root, lst = []):

    if root:
        post_order(root.left)
        post_order(root.right)
        lst.append(root.val)

    return lst

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(4)
root.right.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(8)
root.left.left.left = TreeNode(1)

print(pre_order(root))
print(in_order(root))
print(post_order(root))