class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)  # [0,0,0,0,0]

        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i + 1])

        return dp[0]


# Recursive
# Solution(TLE)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        last = len(triangle) - 1
        mn = float('inf')

        def dfs(row, col):
            if row == 0 and col == 0:
                return triangle[0][0]
            try:
                x = triangle[row][col]
            except IndexError:
                return float('inf')
            up = dfs(row - 1, col)
            upDiagonal = dfs(row - 1, col - 1)
            return triangle[row][col] + min(up, upDiagonal)

        for i in range(len(triangle[last])):
            mn = min(dfs(last, i), mn)
        return mn


# Memoization(DP)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        d = {}
        last = len(triangle) - 1
        mn = float('inf')

        def dfs(row, col):
            if row == 0 and col == 0:
                return triangle[0][0]
            try:
                x = triangle[row][col]
            except IndexError:
                return float('inf')
            if (row - 1, col) in d:
                up = d[(row - 1, col)]
            else:
                up = dfs(row - 1, col)
            if (row - 1, col - 1) in d:
                upDiagonal = d[(row - 1, col - 1)]
            else:
                upDiagonal = dfs(row - 1, col - 1)
            ans = triangle[row][col] + min(up, upDiagonal)
            d[(row, col)] = ans
            return ans

        for i in range(len(triangle[last])):
            mn = min(dfs(last, i), mn)
        return mn