#WAY 1  Using Recursive Approach

class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1: return n
        else: return self.fib(n-1)+self.fib(n-2)


#WAY 2
class Solution:
    memo = {}
    def fib(self, n: int) -> int:
        # if previous calculation stored in memo
        if n in self.memo:
            return self.memo[n]
        # base case
        if n == 0 or n == 1:
            return n
        # otherwise, perform calculation & save value in memo
        self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]