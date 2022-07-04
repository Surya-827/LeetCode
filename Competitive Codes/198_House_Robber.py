#WAY 1
class Solution:
    def rob(self, nums: List[int]) -> int:
        mp={}
        def dp(i):
            if i==len(nums)-1:
                return nums[-1]
            if i>len(nums)-1:
                return 0
            if i+2 not in mp:
                mp[i+2]=dp(i+2)
            if i+1 not in mp:
                mp[i+1]=dp(i+1)
            return max(mp[i+1],mp[i+2]+nums[i])
        return dp(0)

#WAY 2
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2