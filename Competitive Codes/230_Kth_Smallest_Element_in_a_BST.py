def inorder(root, a):
    if root == None:
        return a
    inorder(root.left, a)
    a.append(root.val)
    inorder(root.right, a)
    return a


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a = []
        a = inorder(root, a)
        return a[k - 1]