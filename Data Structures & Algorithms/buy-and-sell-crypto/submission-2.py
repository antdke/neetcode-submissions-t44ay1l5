class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy_price = prices[0]

        for curr_sell_price in prices:
            max_profit = max(max_profit, curr_sell_price - min_buy_price)
            min_buy_price = min(min_buy_price, curr_sell_price)
        return max_profit