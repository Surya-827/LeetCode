class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        out = [[float('inf') for j in range(len(mat[i]))] for i in range(len(mat))]

        # Populate min. distance to the next zero (left/up), set infinity if no zero so far
        if mat[0][0] == 0:
            out[0][0] = 0

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    out[i][j] = 0
                else:
                    if i > 0 and j > 0:
                        out[i][j] = 1 + min(out[i - 1][j], out[i][j - 1])
                    elif i > 0:
                        out[i][j] = 1 + out[i - 1][j]
                    elif j > 0:
                        out[i][j] = 1 + out[i][j - 1]

        # Calculate min distance to the next zero (right/down)
        for i in reversed(range(len(mat))):
            for j in reversed(range(len(mat[i]))):
                if out[i][j] != 0:
                    if i < len(mat) - 1 and j < len(mat[i]) - 1:
                        out[i][j] = min(1 + min(out[i + 1][j], out[i][j + 1]), out[i][j])
                    elif i < len(mat) - 1:
                        out[i][j] = min(1 + out[i + 1][j], out[i][j])
                    elif j < len(mat[i]) - 1:
                        out[i][j] = min(1 + out[i][j + 1], out[i][j])

        return out