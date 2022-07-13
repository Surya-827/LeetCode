
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

#WAY 3
class Solution:
    def reverseBits(self, n: int) -> int:
        sign = 1 if n > 0 else -1

        n = abs(n)
        ans = 0
        k = 31

        while n > 0:
            ans = ans + (n % 2) * 2 ** k
            k -= 1
            n //= 2

        return sign * ans