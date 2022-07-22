class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pre,n,ma=0,len(nums)-1,nums[0]
        while ma<n:
            if pre==ma:break
            pre,ma=ma,max(i+nums[i] for i in range(pre+1,ma+1))
        else:return True
        return False