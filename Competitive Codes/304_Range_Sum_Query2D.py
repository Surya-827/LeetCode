import numpy
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = numpy.array(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        submat = self.mat[row1:row2+1, col1:col2+1]
        sums = numpy.sum(submat, axis = 0)
        return sum(sums)