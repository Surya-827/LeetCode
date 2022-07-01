class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(str(int("".join(str(i) for i in digits)) + 1))