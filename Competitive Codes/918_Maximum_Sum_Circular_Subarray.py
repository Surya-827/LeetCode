class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadanes(arr: List[int]) -> int:
            maxi, sum = float('-inf'), 0
            for i in range(len(arr)):
                sum += arr[i]
                maxi = max(maxi, sum)
                if sum < 0: sum = 0
            return maxi

        arr_sum, res = 0, kadanes(nums)

        if res < 0: return res

        for i in range(len(nums)):
            arr_sum += nums[i]
            nums[i] = -nums[i]

        res = max(arr_sum - (-kadanes(nums)), res)
        return res