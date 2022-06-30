import re

class Solution:
    def myAtoi(self, s: str) -> int:
        # ^ matches beginging of string
        # \s* any nunber of whitspaces (zero or more)
        # [+-] either a + or -
        # [+-]? zero or one of either +/-
        # \d a digit
        # \d + one or more digit
        # the the pattern inside () is a group where you can access

        REGEX = r'^\s*([-+]?\d+)'
        MAX = 2147483647
        MIN = -2147483648

        if not re.search(REGEX, s):
            return 0
        num = int(re.findall(REGEX, s)[0])  # first_match
        return min(MAX, max(num, MIN))