class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        cache = {}

        def mxProf(i, st):
            if i >= len(prices):
                return 0

            if (i, st) in cache:
                return cache[(i, st)]

            if st:
                buy = mxProf(i + 1, not st) - prices[i]
                cool = mxProf(i + 1, st)

                res = max(buy, cool)
            else:
                sell = mxProf(i + 1, not st) + prices[i] - fee
                cool = mxProf(i + 1, st)

                res = max(sell, cool)

            cache[(i, st)] = res
            return res

        return mxProf(0, True)