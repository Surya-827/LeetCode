class Solution:

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
        else:
            if val < root.val:
                if root.left is not None:
                    self.insertIntoBST(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right is not None:
                    self.insertIntoBST(root.right, val)
                else:
                    root.right = TreeNode(val)

        return root