from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        del salary[salary.index(min(salary))]
        del salary[salary.index(max(salary))]
        return sum(salary)/len(salary)

if __name__=="__main__":

    obj = Solution()
    sal = list(map(int,input().split()))
    print(obj.countOddNumbers(sal))