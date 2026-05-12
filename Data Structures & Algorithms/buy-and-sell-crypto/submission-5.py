class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        lowest_price = prices[0]
        profit = 0

        for price in prices:
            profit = max(profit, price - lowest_price)
            lowest_price = min(lowest_price, price)

        return profit


