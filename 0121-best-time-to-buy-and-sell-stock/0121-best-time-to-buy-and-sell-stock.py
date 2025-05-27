class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_profit=float('inf')
        n=len(prices)
        profit=0
        for i in range(n):
            if prices[i] < min_profit:
                min_profit=prices[i]
            else:
                profit=prices[i]-min_profit
            if profit>max_profit:
                max_profit=max(profit,max_profit)
        return max_profit               

            