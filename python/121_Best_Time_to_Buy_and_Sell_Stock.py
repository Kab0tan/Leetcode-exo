class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = prices[0]
        profit = 0
        for price in prices:
            if price < min and price != prices[-1]:
                min = price
                max = price
            if  price > max:
                max = price
            if max-min > profit:
                profit = max-min
        return profit
