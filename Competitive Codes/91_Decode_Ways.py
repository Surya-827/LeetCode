#Simple Way

# def numDecodings(self, s: str) -> int:
#     last1 = 1 if s[-1] != '0' else 0
#     last2 = 1

#     for i in range(len(s) - 2, -1, -1):
#         curr = 0
#         if s[i] != '0':
#             if int(s[i:i+2]) <= 26: curr = last2
#             last1, last2 = curr + last1, last1
#         else: last1, last2 = 0, last1

#     return last1


class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        n = len(s)

        def dfs(curr):
            if curr >= n: return 1

            if curr in memo: return memo[curr]
            ans = 0

            if s[curr] != '0':
                ans = dfs(curr + 1)
                if curr + 1 < n and int(s[curr:curr + 2]) <= 26:
                    ans += dfs(curr + 2)

            memo[curr] = ans

            return memo[curr]

        return dfs(0)