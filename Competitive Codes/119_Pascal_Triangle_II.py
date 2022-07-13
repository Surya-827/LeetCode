class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        firstRow = [1]
        res = firstRow

        for i in range(1, rowIndex + 1):
            prevRow = res
            currentRow = []
            currentRow.append(1)
            for j in range(1, i):
                currentRow.append(prevRow[j - 1] + prevRow[j])
            currentRow.append(1)

            res = currentRow

        return res


# RECURSIVE
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return findRow(rowIndex)


def findRow(rowIndex):
    if (rowIndex == 0):
        return [1]
    elif (rowIndex == 1):
        return [1, 1]
    else:
        prevRow = findRow(rowIndex - 1)
        currentRow = []
        currentRow.append(1)
        for j in range(1, rowIndex):
            currentRow.append(prevRow[j - 1] + prevRow[j])
        currentRow.append(1)
        return currentRow