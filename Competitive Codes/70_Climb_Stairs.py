class Solution:
    def climbStairs(self, n: int) -> int:
        ans = {
            1:1,
            2:2,
            3:3
        }
        def solve(n):
            if n in ans.keys():
                return ans[n]
            else:
                ans[n] = int(solve(n-1)) + int(solve(n-2))
                return ans[n]
        return solve(n)