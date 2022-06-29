import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        r = re.search(p,s)
        if r and r.group(0) == s:
            return True
        return False

