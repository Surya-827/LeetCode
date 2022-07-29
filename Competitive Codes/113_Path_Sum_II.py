class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        result = []

        def dfs(root, target, path):
            if not root:
                return
            if not root.left and not root.right and target - root.val == 0:
                result.append(path + [root.val])
                return

            dfs(root.left, target - root.val, path + [root.val])
            dfs(root.right, target - root.val, path + [root.val])

        dfs(root, target, [])
        return result