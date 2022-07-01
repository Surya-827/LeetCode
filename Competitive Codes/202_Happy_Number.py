class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:return True
        while n > 2:
            n = sum(int(i)**2 for i in str(n))
            if n == 1:return True
            if n == 4:return False
        return False