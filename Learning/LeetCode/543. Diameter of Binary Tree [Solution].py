class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def height(node) -> int:
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)

            # Update the diameter if the path through the current node is larger
            self.diameter = max(self.diameter, left_height + right_height)

            # Return the height of the current node
            return 1 + max(left_height, right_height)

        height(root)
        return self.diameter


# Test Builder helper

def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# Test Case - Empty tree
root = None
print(Solution().diameterOfBinaryTree(root))  # Expected Output: 0


# Test Case 2 - Single node tree
root = TreeNode(1)
print(Solution().diameterOfBinaryTree(root))  # Expected Output: 0

# Test Case 3
root = build_tree([1, None, 2, None, 3])
print(Solution().diameterOfBinaryTree(root))  # Expected Output: 2

# Test Case 4
root = build_tree([1, 2, None, 3])
print(Solution().diameterOfBinaryTree(root))  # Expected Output: 2

# Test Case 5
root = build_tree([1, 2, 3, 4, 5, None, 6])
print(Solution().diameterOfBinaryTree(root))  # Expected Output: 3

# Test Case 6
root = build_tree([1, 2, 3, 4, None, None, 6, 5])
print(Solution().diameterOfBinaryTree(root))  # Expected Output: 4

# Test Case 7
root = build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, None, 9])
print(Solution().diameterOfBinaryTree(root))  # Expected Output: 6


# Test case 8 - From leetcode
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution().diameterOfBinaryTree(root))