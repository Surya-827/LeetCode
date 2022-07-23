class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        held, sold, reset = float('-inf'), float('-inf'), 0

        for price in prices:
            held = max(held, reset - price)

            prev_sold = sold
            sold = max(sold, held + price)

            reset = max(reset, prev_sold)

        return max(reset, sold)