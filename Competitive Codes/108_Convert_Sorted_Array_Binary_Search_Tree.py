class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums) == 1:
            return TreeNode(nums[0])

        if len(nums) == 0:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root