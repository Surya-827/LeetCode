class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        nums1 = nums[:-1]
        nums2 = nums[1:]

        def basicRob(nums):
            case1 = case2 = 0
            for n in nums:
                temp = case2
                case2 = case1 + n
                case1 = max(case1, temp)
            return max(case1, case2)

        return max(basicRob(nums1), basicRob(nums2))