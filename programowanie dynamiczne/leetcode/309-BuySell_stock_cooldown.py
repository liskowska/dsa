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

    def rec(i, state):
        if i == len(prices): return 0

        if state == "buy":   # mam akcję
            return max(rec(i+1, "cooldown"), rec(i+1, "sell") + prices[i])
        elif state == "sell": # właśnie sprzedałem → cooldown
            return rec(i+1, "cooldown")
        elif state == "cooldown": # mogę kupić lub odpocząć
            return max(rec(i+1, "cooldown"), rec(i+1, "buy") - prices[i])
    return rec(0, "cooldown")

prices1= [1,2,3,0,2]
print(maxProfit(prices1))

prices2 = [4,3,2,10,11,0,11]
print(maxProfit(prices2))