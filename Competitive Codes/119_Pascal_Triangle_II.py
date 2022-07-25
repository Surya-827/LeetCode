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

#Way 4
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        current = [1, 1]
        for i in range(rowIndex - 1):
            lst = [1]
            l = 0
            while l < (len(current) - 1):
                lst.append(current[l] + current[l + 1])
                l += 1

            lst.append(1)
            current = lst

        return current