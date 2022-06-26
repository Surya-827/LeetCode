
# WAY 1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSameTree(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            return p.val == q.val and isSameTree(p.left, q.right) and isSameTree(p.right, q.left)
        return isSameTree(root.left, root.right)

# WAY 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if (root is None):
            return false

        leftRoot, rightRoot = TreeNode(), TreeNode()
        if (root.left is not None):
            leftRoot = root.left
        if (root.right is not None):
            rightRoot = root.right

        if ((leftRoot is None and rightRoot is not None) or (rightRoot is None and leftRoot is not None)):
            return False

        leftList, rightList = [root], [root]

        while (len(leftList) > 0 and len(rightList) > 0):
            leftSide = leftList.pop(0)
            rightSide = rightList.pop(0)

            if (leftSide is not None and rightSide is not None):
                if (leftSide.val != rightSide.val):
                    return False

                leftList.append(leftSide.left)
                leftList.append(leftSide.right)

                rightList.append(rightSide.right)
                rightList.append(rightSide.left)
            elif ((leftSide is None and rightSide is not None) or (leftSide is not None and rightSide is None)):
                return False

        return True