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

#Way - 3
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = []
        for x in range(numRows):
            a.append([1])
            # 			creating the 2d array
            # 			appending the starting 1: [1, ...]
            if x > 1:
                # 			skipping the first two rows
                for c in range(x - 1):
                    # 					for loop used to find info about previous row
                    a[x].append(a[x - 1][c] + a[x - 1][c + 1])
            # 					math for adding the c and the c+1 number from the previous row
            if x > 0:
                # 			checking if its not the first row
                a[x].append(1)
        # 				appending the ending 1: [1, ..., 1]
        return a

# Version with no comments
#         a = []
#         for x in range(numRows):
#             a.append([1])
#             if x > 1:
#                 for c in range(x-1):
#                     a[x].append(a[x-1][c]+a[x-1][c+1])
#             if x > 0:
#                 a[x].append(1)
#         return a

if __name__=="__main__":

    n = int(input())
    s = Solution()
    print(s.generate(n))
