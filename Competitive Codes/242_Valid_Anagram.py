class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(list(s))
        b = sorted(list(t))

        return True if a == b else False