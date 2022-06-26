
# WAY 1

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val] if root else []

# way 2
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def recursive(root):
            nodes = []

            if not root:
                return nodes

            if root.left:
                nodes += recursive(root.left)

            if root.right:
                nodes += recursive(root.right)

            nodes.append(root.val)

            return nodes

        def iterative(root):
            nodes = []

            if not root:
                return nodes

            stack = [root]

            while stack:
                curr = stack.pop()
                nodes.append(curr.val)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)

            return nodes[::-1]

        return iterative(root)