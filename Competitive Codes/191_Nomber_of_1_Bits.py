class Solution:
    def hammingWeight(self, n: int) -> int:
        t = bin(n)
        return str(t).count('1')
