import ast

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        dic = {}
        stack = []
        if root:
            stack.append((1, root))

        while stack:
            idx, node = stack.pop()
            dic[idx] = node.val
            if node.left:
                stack.append((2 * idx, node.left))
            if node.right:
                stack.append((2 * idx + 1, node.right))
        return str(dic)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # convert dictionary string back to dictionary
        dic = ast.literal_eval(data)

        def buildTree(idx):
            if idx not in dic:
                return
            node = TreeNode(dic[idx])
            node.left = buildTree(2 * idx)
            node.right = buildTree(2 * idx + 1)
            return node

        return buildTree(1)