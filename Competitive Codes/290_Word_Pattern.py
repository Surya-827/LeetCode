class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h = {}

        s = s.split(" ")
        pattern = list(pattern)

        if (len(s) != len(pattern)):
            return 0

        for i, j in zip(pattern, s):
            if i not in h:
                if j not in h.values():
                    h[i] = j
                else:
                    return 0
            else:
                if (h[i] != j):
                    return 0

        return 1