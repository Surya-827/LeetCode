class Solution:

    # root is the current visited node, nextNode is the node that root needs to connect to
    def visit(self, root, nextNode):

        if not root:
            return

        # connnect root to next node
        if (nextNode):
            root.next = nextNode

        # the next node for the left node is the right one
        self.visit(root.left, root.right)

        # if we have a next node, the right node will need to be connected to its left node
        if (nextNode):
            self.visit(root.right, nextNode.left)
        else:
            self.visit(root.right, None)

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.visit(root, None)

        return root