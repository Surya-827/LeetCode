# WAY 1

def isBalanced(self, root: Optional[TreeNode]) -> bool:
    res = True

    def balanced_helper(node):
        nonlocal res
        if not node:
            return -1
        left_height = balanced_helper(node.left)
        right_height = balanced_helper(node.right)
        if abs(left_height - right_height) > 1:
            res = False
        current_height = max(left_height, right_height) + 1
        return current_height

    balanced_helper(root)
    return res

# WAY 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        return self.isBalanced(root.right) and self.isBalanced(root.left)

    def height(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + max(self.height(root.left), self.height(root.right))