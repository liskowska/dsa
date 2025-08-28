"""
309. Best time to buy and sell stock with cooldown
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).
"""

def maxProfit(prices):
    dp = {} # key = (i, buing)  val = max_profit
    def rec(i, buying):
        if i >= len(prices): return 0
        if (i, buying) in dp: return dp[(i, buying)]

        if buying:
            buy = rec(i+1, not buying) - prices[i]
            cooldown = rec(i+1, buying)
            dp[(i, buying)] = max(buy, cooldown)

        else: # not buying ==> selling
            sell = rec(i+2, not buying) + prices[i]
            cooldown = rec(i+1, buying)
            dp[(i, buying)] = max(sell, cooldown)

        return dp[(i, buying)]
    return rec(0, True)

prices1= [1,2,3,0,2]
print(maxProfit(prices1))

prices2 = [4,3,2,10,11,0,11]
print(maxProfit(prices2))

prices3 = [1, 2, 4]
print(maxProfit(prices3))