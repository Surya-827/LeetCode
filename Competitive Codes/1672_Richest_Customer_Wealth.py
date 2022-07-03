
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res =[]
        for i in accounts:
            res.append(sum(i))
        return max(res)


