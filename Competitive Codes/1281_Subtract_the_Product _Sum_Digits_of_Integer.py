from functools import reduce as r

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(i) for i in str(n)]
        prod = r((lambda x,y:x*y),digits)
        add = sum(digits)
        return prod-add