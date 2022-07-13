class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 1
        end = num
        while start <= end:
            mid = (start + end) // 2
            if mid**2 > num:
                end = mid-1
            elif mid**2 < num:
                start = mid+1
            else:
                return True
        return False