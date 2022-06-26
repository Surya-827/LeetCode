#WAY 1

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nums = "".join(map(str,range(1, n+1)))
        @lru_cache(maxsize=None)
        def dfs(nums):
            if not nums:  return [None]
            res = []
            for idx in range(len(nums)):
                lefts = dfs(nums[:idx])
                rights = dfs(nums[idx+1:])
                res += [ TreeNode(nums[idx], l,r )for l in lefts for r in rights]
            return res

        return dfs(nums)

#WAY 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def genTreesDP(self, dp, nodes):
        if nodes in dp: return dp[nodes]

        node_list = nodes.split("_")
        node_list = [int(i) for i in node_list]

        if len(node_list) == 1:
            tmp = TreeNode(node_list[0])
            dp[nodes] = [tmp]
            return dp[nodes]

        # for each, take the ones to the left and right
        all_tree = []
        for i in range(len(node_list)):
            left = [str(n) for n in node_list[:i]]
            right = [str(n) for n in node_list[i + 1:]]

            left_tree = self.genTreesDP(dp, "_".join(left))
            right_tree = self.genTreesDP(dp, "_".join(right))

            for l in left_tree:
                for r in right_tree:
                    tmp_root = TreeNode(node_list[i], l, r)
                    all_tree.append(tmp_root)

        dp[nodes] = all_tree
        return all_tree

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}
        node_list = list(range(1, n + 1))
        node_list = [str(i) for i in node_list]
        dp[""] = [None]
        return self.genTreesDP(dp, "_".join(node_list))