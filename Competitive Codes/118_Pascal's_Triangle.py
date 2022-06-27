from collections import defaultdict
from typing import List

# WAY 1
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1,numRows+1):
            arr = [1] * i
            ans = self.solve(arr, i)
            res.append(ans)
        return res

    def solve(self,arr,numRows):
        for i in range(numRows):
            if(i==0 or i==numRows-1):
                continue
            if(i%2==0):
                arr[i] = arr[i]+numRows
            if(i%2==1):
                arr[i] = abs(arr[i]-numRows)
        return arr

# WAY 2
class Solution:
    def generate(self,rowIndex:int)->List[List[int]]:
        lst = defaultdict(list)
        # Base Case
        if rowIndex == 0:
            return [1]
        # Recursive Solution
        temp = [0] + self.generate(rowIndex - 1) + [0]
        for i in range(len(temp) - 1):
            lst[rowIndex].append(temp[i] + temp[i + 1])
        return lst[rowIndex]

if __name__=="__main__":

    n = int(input())
    s = Solution()
    print(s.generate(n))
