import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(math.floor(math.sqrt(i)), 0, -1):
                dp[i] = min(dp[i], 1 + dp[i-(j*j)])
        return dp[-1]
