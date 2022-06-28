
class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        def Palindrome(s: str, l: int, r: int) -> int:
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return r - l - 1

        start = 0
        end = 0
        for i in range(0, len(s)):
            len1 = Palindrome(s, i, i)
            len2 = Palindrome(s, i, i + 1)
            len3 = max(len1, len2)
            if (len3 > end - start):
                start = i - (len3 - 1) // 2
                end = i + len3 // 2
        return s[start: end + 1]