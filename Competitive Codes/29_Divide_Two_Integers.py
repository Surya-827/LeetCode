import math as m


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        check = False
        if dividend < 0 or divisor < 0:
            check = True

        if dividend < 0 and divisor < 0:
            check = False
        res = abs(dividend) // abs(divisor)
        if check:
            res = -res

        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        return res