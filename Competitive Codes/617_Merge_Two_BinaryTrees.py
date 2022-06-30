

class Solution(object):
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 and root2:
            tree = TreeNode(root1.val+root2.val)
            tree.left = self.mergeTrees(root1.left,root2.left)
            tree.right = self.mergeTrees(root1.right,root2.right)

        elif(root1 and not root2):
            tree = TreeNode(root1.val)
            tree.left = self.mergeTrees(root1.left,None)
            tree.right = self.mergeTrees(tree.right,None)

        elif(root2 and not root1):
            tree = TreeNode(root2.val)
            tree.left = self.mergeTrees(None,root2.left)
            tree.right = self.mergeTrees(None,root2.right)
        else:
            return None
        return tree

