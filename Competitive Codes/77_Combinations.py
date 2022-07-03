
#WAY 1

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []

        def bt(l, k, path):
            if len(path) == k:
                self.res.append(path)
                return

            for i in range(len(l)):
                bt(l[i + 1:], k, path + [l[i]])
        bt([x for x in range(1, n + 1)], k, [])
        return self.res


#WAY 2
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        return list(combinations(nums,k))