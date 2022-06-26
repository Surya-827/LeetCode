# WAY 1

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        if root == None:
            return l
        return self.inorderT(root,l)
    def inorderT(self,root,l):
        if root:
            self.inorderT(root.left,l)
            l.append(root.val)
            self.inorderT(root.right,l)
        return l

# WAY 2
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    stack = []
    current_node = root
    while ((current_node is not None) or (stack)):
        while (current_node is not None):
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        res.append(current_node.val)
        current_node = current_node.right
    return res