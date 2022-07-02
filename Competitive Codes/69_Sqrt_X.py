
#WAY 1
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))

# WAY 2
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        if x==0 or x==1:
            return x

        while left <= right:
            mid = left + (right-left)//2
            testvalue = mid*mid

            if testvalue == x:
                return mid
            if testvalue < x:
                left = mid + 1
            else:
                right = mid -1

        return left-1