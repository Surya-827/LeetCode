class Solution(object):
    def longestPalindrome(self, s):
        used = []
        length = 0
        for x in s:
            if x not in used:
                used.append(x)
            else:
                length += 2
                used.remove(x)

        if len(used) > 0:
            length += 1

        return length