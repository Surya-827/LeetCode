#WAY 1 Using Math
import math


# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#         edges = (high%2) + (low%2)
#         middle = math.floor((high-low-1)/2)
#         return edges + middle + 1 if edges == 0 else edges + middle


# Way 2 Using Anonymous Function
class Solution:
    def countOdds(self,low:int,high:int) -> int:
        c = 0

        check = lambda x  : 1 if x%2==1 else 0
        for i in range(low,high+1):
            if(check(i)==1):
                c+=1
        return c

#Way 3 Using List Comprehnsion
# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#         c = [1 if(i%2==1) for i in range(low,high+1)]
#         return sum(c)