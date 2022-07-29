class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        # recursion in pre-order : conditions

        # first value in pre-order traversal is root


        # recursion in in-order : conditions

        # every value to the left of the in-order root will go into left sub-tree

        # every value to the right of the in-order root will go into rigth sub-tree

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root