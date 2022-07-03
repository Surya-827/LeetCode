class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        stack, output = [root], []
        while stack:
            temp = []
            temp_stack = []
            for node in stack:
                temp.append(node.val)
                if node.left:
                    temp_stack.append(node.left)
                if node.right:
                    temp_stack.append(node.right)
            stack = temp_stack
            output.append(temp)

        return output