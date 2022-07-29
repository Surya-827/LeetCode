class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        markset = []
        stack = []
        for i, c in enumerate(s):
            if c not in '()':
                continue
            if c == '(':
                stack.append(i)
            elif not stack:
                markset.append(i)
            else:
                stack.pop()

        markset = markset + stack

        res = ''

        for i in range(len(s)):
            if i not in markset:
                res += s[i]

        return res