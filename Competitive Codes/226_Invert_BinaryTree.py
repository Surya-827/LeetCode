# way 1

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root is None or (root.right is None and root.left is None)):
            return root
        temp = root.left
        root.left = root.right
        root.right = temp;
        root.right = self.invertTree(root.right)
        root.left = self.invertTree(root.left)
        return root


# way 2
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # time complexity: O(N)
        # space complexity: O(logN)
        # dfs
        if root is None:
            return None

        # swap left and right subtree
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs
        # time complexity: O(N)
        # space complexity: O(l), where l is the maximum number of nodes in a level
        if not root:
            return None
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            node.left, node.right = node.right, node.left
            if node.left:
                q.put(node.left)

            if node.right:
                q.put(node.right)

        return root