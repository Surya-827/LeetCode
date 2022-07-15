class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if (len(matrix) == 1):
            return matrix[0]
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0
        ans = []
        while (left <= right and top <= bottom):
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1

        n = len(matrix[0]) * len(matrix)
        print(n)
        print(len(ans))
        if (n == len(ans)):
            return ans
        else:
            return ans[0:n]