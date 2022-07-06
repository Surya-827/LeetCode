class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = list()

        self.DFS(root, values)

        for i in range(1, len(values)):
            if not values[i] > values[i - 1]:
                return False

        return True

    def DFS(self, node, array):
        if not node:
            return

        self.DFS(node.left, array)
        array.append(node.val)
        self.DFS(node.right, array)