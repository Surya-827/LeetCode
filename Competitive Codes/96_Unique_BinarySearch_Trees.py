#WAY 1

class Solution:

    def numTrees(self, n: int) -> int:
        question_bank = {}
        def fun(n):
            if n == 0 or n == 1:
                return 1
            if n == 2:
                return 2
            if n in question_bank:
                return question_bank[n]
            count = 0
            for i in range(1, n+1):
                left = i - 1
                right = n - i
                sub_left = fun(left)
                sub_right = fun(right)
                count += sub_left * sub_right
            question_bank[n] = count
            return question_bank[n]
        return fun(n)

#WAY 2

class Solution:
    def numTrees(self, n: int) -> int:
        # The empty tree is the only tree with 0 nodes.
        dp = [1]
        for i in range(1, n + 1):
            dp.append(0)
            for k in range(0, i):
                dp[i] += (dp[k] * dp[i - k - 1])
        return dp[n]