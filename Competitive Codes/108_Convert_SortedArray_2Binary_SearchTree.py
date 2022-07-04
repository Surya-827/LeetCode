# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, None, 0, len(nums) - 1)

    def helper(self, nodes, tree, left, right):
        # base case
        if right < left:
            return
        mid = (left + right) // 2
        # get mid and add value at mid to tree
        tree = TreeNode(nodes[mid])
        # repeat for left side
        tree.left = self.helper(nodes, tree, left, mid - 1)
        # repeat for right side
        tree.right = self.helper(nodes, tree, mid + 1, right)
        return tree