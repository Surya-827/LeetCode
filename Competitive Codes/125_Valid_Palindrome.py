
#WAY 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlnum(s[l]):
                l += 1
            while l < r and not self.isAlnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def isAlnum(self, c: str) -> bool:
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))

#WAY 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ','')
        s=s.lower()
        s = [x for x in s if x.isalnum()]
        return list(s)==list(s)[::-1]