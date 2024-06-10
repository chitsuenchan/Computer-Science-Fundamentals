"""
    Passed easily

    Difficulty 2/10
"""

from HelperClasses.BinaryTree import TreeNode

class BSTIterator:

    def __init__(self, root):
        self.root = root
        self.lst = self.in_order(self.root)
        self.current_idx = 0

    def next(self) -> int:
        val = self.lst[self.current_idx]
        self.current_idx += 1
        return val

    def hasNext(self) -> bool:
        if self.current_idx in range(len(self.lst)):
            return True
        else:
            return False

    def in_order(self, root, lst=None):

        if lst is None:
            lst = []
        if root:
            self.in_order(root.left, lst)
            lst.append(root.val)
            self.in_order(root.right, lst)

        return lst



root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

bst = BSTIterator(root)
print(bst.lst)
print(bst.next())
print(bst.next())
print(bst.next())
print(bst.next())
print(bst.hasNext())

