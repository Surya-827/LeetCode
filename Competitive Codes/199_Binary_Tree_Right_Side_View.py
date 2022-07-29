class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = [root]
        ans = []

        while q:
            n = len(q)
            for i in range(n):
                curnode = q.pop(0)
                if i == n-1:  #Adding last node
                    ans.append(curnode.val)
                if curnode.left:
                    q.append(curnode.left)
                if curnode.right:
                    q.append(curnode.right)
        return ans