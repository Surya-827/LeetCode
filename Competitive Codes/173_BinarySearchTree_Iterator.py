class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.get_inorder(root)

    def next(self) -> int:
        return self.stack.pop(0)

    def hasNext(self) -> bool:
        if self.stack:
            return True
        else:
            return False

    def get_inorder(self, node) -> None:
        if node:
            self.get_inorder(node.left)
            self.stack.append(node.val)
            self.get_inorder(node.right)