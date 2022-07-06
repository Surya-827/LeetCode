class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def check(n1, n2):
            if not n1 or not n2:
                return False
            if n1.val + n2.val == k:
                # same node is wrong
                if n1 != n2:
                    return True
                # one toward bigger, the other toward smaller
                return check(n1.right, n2.left) or check(n1.left, n2.right)
            elif n1.val + n2.val < k:
                # look for bigger value node
                return check(n1.right, n2) or check(n1, n2.right)
            elif n1.val + n2.val > k:
                # look for smaller value node
                return check(n1.left, n2) or check(n1, n2.left)

        return check(root, root)


# Using
# hash
# table
# for two sum questions:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()

        def traversal(node):
            if not node:
                return False
            if k - node.val in s:
                return True
            s.add(node.val)
            return traversal(node.left) or traversal(node.right)

        return traversal(root)