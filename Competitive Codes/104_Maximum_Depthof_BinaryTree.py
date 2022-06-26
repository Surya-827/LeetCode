
#WAY 1
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            if left > right:
                return left + 1
            else:
                return right + 1

# way 2