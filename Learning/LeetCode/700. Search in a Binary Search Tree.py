"""
    Used a while iterative approach
    This is because the depth of the tree can be longer than 1000
    and this will maxx out the recursion
"""

def searchBST(root, val):
    while root:
        if root.val == val:
            return root
        elif root.val < val:
            root = root.right
        else:
            root = root.left
    return None

