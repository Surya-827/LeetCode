class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        mx, mn = [1]*n, [1]*n
        mx[0] = mn[0] = nums[0]
        ans = max(mx[0], mn[0])
        for i in range(1, n):
            mx[i] = max(nums[i], max(mx[i-1]*nums[i], mn[i-1]*nums[i]))
            mn[i] = min(nums[i], min(mx[i-1]*nums[i], mn[i-1]*nums[i]))
            ans = max(ans, max(mx[i], mn[i]))
        return ans