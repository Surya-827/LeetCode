class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if not root:
                return None
            else:
                if (p.val > root.val and q.val > root.val):
                    return helper(root.right)
                if (p.val < root.val and q.val < root.val):
                    return helper(root.left)
                else:
                    return root

        return helper(root)