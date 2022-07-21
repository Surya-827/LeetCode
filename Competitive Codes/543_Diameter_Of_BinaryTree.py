class Solution(object):
    def height(self, root):
        if not root:
            return 0
        stack = [(0, root)]
        max_height = 0
        while stack:
            current_height, current_node = stack.pop()
            max_height = max(max_height, current_height)
            if current_node:
                stack.append((current_height + 1, current_node.left))
                stack.append((current_height + 1, current_node.right))
        return max_height

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = [(0, root)]
        max_diam = 0

        while stack:
            cur_diam, cur_node = stack.pop()

            # checks the diameter for sub trees
            if cur_node.left:
                stack.append((cur_diam + 1, cur_node.left))
            if cur_node.right:
                stack.append((cur_diam + 1, cur_node.right))

            # Checks the diameter through the root node
            di_root = self.height(cur_node.left) + self.height(cur_node.right)

            # Max of either subtree or through root node
            max_diam = max(max_diam, max(di_root, cur_diam))

        return max_diam