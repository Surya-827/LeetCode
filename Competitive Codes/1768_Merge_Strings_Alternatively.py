class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        size = len(word1)

        if len(word1) > len(word2):
            size = len(word2)
        else:
            size = len(word1)

        res = ""

        for i in range(0, size):
            res += word1[i]
            res += word2[i]

        res += word1[size:]
        res += word2[size:]

        return res