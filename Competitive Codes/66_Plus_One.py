class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ans = []
        for i in range(len(digits)-1, -1, -1):
            a = digits[i] + carry
            if len(str(a)) == 2:
                carry = int(str(a)[0])
                a = int(str(a)[1])
            else:
                carry = 0
            ans.append(a)
        if carry:
            ans.append(carry)
        return ans[::-1]