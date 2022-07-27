class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[0] * n for _ in range(m)]
        res[0][0] = sum([mat[r][c] for r in range(0, min(m, k + 1)) for c in range(0, min(n, k + 1))])
        for i in range(m):
            if i != 0:
                res[i][0] = res[i - 1][0]
                if i - k - 1 >= 0:
                    res[i][0] -= sum(mat[i - k - 1][0:min(m, k + 1)])
                if i + k < m:
                    res[i][0] += sum(mat[i + k][0:min(m, k + 1)])
            for j in range(1, n):
                res[i][j] = res[i][j - 1]
                if j - k - 1 >= 0:
                    res[i][j] -= sum([mat[ii][j - k - 1] for ii in range(max(0, i - k), min(m, i + k + 1))])
                if j + k < n:
                    res[i][j] += sum([mat[ii][j + k] for ii in range(max(0, i - k), min(m, i + k + 1))])
        return res