class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            profits.append(price - min_price)
        
        return max(profits)