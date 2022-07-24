#Way 1 Using Greedy approach

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp=[0 for i in range(len(nums)-1)]
        dp2=[0 for i in range(len(nums))]
        for i in range(len(nums)-1):
            dp[i]=nums[i]-nums[i+1]
        for i in range(len(dp)):
            flag=0
            for j in range(i+1,len(dp)):
                if(dp[i]==dp[j]):
                    flag+=1
                else:
                    break
            dp2[i]=flag
        return(sum(dp2))