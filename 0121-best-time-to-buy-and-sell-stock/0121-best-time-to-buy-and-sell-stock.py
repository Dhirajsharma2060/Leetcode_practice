class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_prices=0
        l,r=0,1
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                best_prices=max(best_prices,profit)
            else:
                l=r
            r+=1
        return best_prices            



        