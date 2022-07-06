#WAY 1 Using inbuilt method
'''
class Solution:
    def toLowerCase(self, s: str) -> str: return s.lower()
'''
#WAY 2 User Defined Func

class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""

        for i in s:
            if ord(i) in range(65, 91):
                ans += chr(ord(i) + 32)
            else:
                ans += i
        return ans


if __name__=="__main__":
    obj = Solution()
    s = input()
    print(obj.toLowerCase(s))