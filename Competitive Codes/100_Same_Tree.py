class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both are None return True
        if p == None and q == None:
            return True

        # if both are not none but one of the is none, return false
        elif p == None or q == None:
            return False

        # if both are not none and values ae not same, return false
        elif p.val != q.val:
            return False

        # else check same for left tree and right tree
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)