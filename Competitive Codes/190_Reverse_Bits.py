
#WAY 1
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(str(bin(n)).lstrip("0b").zfill(32)[::-1], 2)

# WAY 2
class Solution:
    def reverseBits(self, n: int) -> int:
        reverseStr = str(bin(n))[::-1][:-2]
        reverseStr += (32-len(reverseStr)) * '0'
        return int(reverseStr, 2)