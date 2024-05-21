class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pre_order(root, result = []):
    if root:
        result.append(root.val)
        pre_order(root.left)
        pre_order(root.right)

    return result

def in_order(root, result = []):
    if root:
        in_order(root.left)
        result.append(root.val)
        in_order(root.right)

    return result

def post_order(root, result = []):
    if root:
        post_order(root.left)
        post_order(root.right)
        result.append(root.val)
    return result

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.right.left = TreeNode(4)
root.right.right = TreeNode(7)
root.right.left.left = TreeNode(2)
root.right.left.right = TreeNode(5)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(10)

print("Pre-order:   ", pre_order(root))
print("In-order:    ", in_order(root))
print("Post-order:  ", post_order(root))

