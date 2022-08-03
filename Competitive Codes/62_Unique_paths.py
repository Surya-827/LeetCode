class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''one liner'''
        return math.comb(m+n-2, m-1)

if __name__=="__main__":

    obj = Solution()
    m,n = map(int,input().split())

    print(obj.uniquePaths(m,n))

