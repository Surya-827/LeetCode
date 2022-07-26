class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        res = float('inf')

        self.memo = [[10001] * n for _ in range(n)]

        for j in range(n):
            res = min(res, self.dp(matrix, n - 1, j))

        return res

    def dp(self, matrix, i, j):

        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix):
            return 10001
        # base case
        if i == 0:
            return matrix[0][j]

        if self.memo[i][j] != 10001:
            return self.memo[i][j]

        self.memo[i][j] = matrix[i][j] + min(self.dp(matrix, i - 1, j), self.dp(matrix, i - 1, j - 1),
                                             self.dp(matrix, i - 1, j + 1))

        return self.memo[i][j]