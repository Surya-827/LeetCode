class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[-2], dp[-1])


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1=cost[0]
        step2=cost[1]
        for i in range(2,len(cost)):
            temp=step2
            step2 = cost[i] + min(step1,step2)
            step1 = temp
        return min(step1,step2)