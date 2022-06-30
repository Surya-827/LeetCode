#WAY 1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1

#WAY 2
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)