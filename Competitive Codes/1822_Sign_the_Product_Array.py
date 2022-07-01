
#WAY 1
from functools import reduce as r
from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = r(lambda x, y: x * y, nums, 1)
        if prod > 0:return 1
        elif (prod == 0):return 0
        else:return -1

# way 2

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        f=1
        for i in nums:
            f*=i
        return [[1 if f>0 else -1][0] if f!=0 else 0][0]