class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1


if __name__=="__main__":
    obj = Solution()
    s = input()
    obj.firstUniqChar(s)