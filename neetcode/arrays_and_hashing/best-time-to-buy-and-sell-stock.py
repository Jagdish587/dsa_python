# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      buy_price = prices[0]
      max_profit = 0

      for current_price in prices[1:]:
        if current_price < buy_price:
            buy_price = current_price

        max_profit = max(max_profit, current_price - buy_price)
      return max_profit  
        