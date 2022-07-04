#WAY 1

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat) # square matrix thus row len = height.
        # sum the primary and secondary diagonals values.
        total = 0
        for i in range(size):
            total += mat[i][i]
            total += mat[i][abs(size-1-i)]
        # subtract the middle number on the secondary diagonal if size is odd.
        if size % 2 == 1:
            total -= mat[size//2][size//2]
        return total


#WAY 2
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat) # square matrix thus row len = height.
        # get the primary and secondary diagonals.
        primary = [mat[i][i] for i in range(size)]
        secondary = [mat[i][abs(size-1-i)] for i in range(size)]
        # remove the middle number for the secondary diagonal if size is odd.
        if size % 2 == 1:
            del secondary[size//2]
        return sum(primary+secondary)