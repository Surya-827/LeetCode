class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        flag = False

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == target:
                    flag = True
        return flag