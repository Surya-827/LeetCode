#WAY 1
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(eval(f"{num1}+{num2}"))

#WAY 2
class Solution(object):
    def stToNum(self,num):
        result = 0
        for i in num:
            result = 10*result + ord(i)-ord('0')
        return result
    def addStrings(self, num1, num2):
        return(str(self.stToNum(num1)+self.stToNum(num2)))