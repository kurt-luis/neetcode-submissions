class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        lowest_price = 101
        profit = 0

        for i in range(len(prices)):
            profit = max(profit, prices[i] - lowest_price)

            lowest_price = min(lowest_price, prices[i])

        return profit


