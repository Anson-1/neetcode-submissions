class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxprofit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxprofit = max(profit, maxprofit)
            else:
                l = r
            r += 1

        return maxprofit



        