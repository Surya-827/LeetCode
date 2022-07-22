class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < len(nums) - 1: # 4
            longest = max([i + nums[i] for i in range(l, r + 1)])
            l, r = r + 1, longest
            res += 1
        return res