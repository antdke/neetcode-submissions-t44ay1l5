class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # track the max profit
        max_profit = 0
        # track the min price seen so far
        min_buy_price = prices[0]

        # every seen price is potential sell price
        # traverse list
        for curr_sell_price in prices:
            # see if diff btwn current sell price and min price seen so far is greatest profit
            max_profit = max(max_profit, curr_sell_price - min_buy_price)
            # update min price we've seen so far if it's lower
            min_buy_price = min(min_buy_price, curr_sell_price)
        # return max price
        return max_profit
