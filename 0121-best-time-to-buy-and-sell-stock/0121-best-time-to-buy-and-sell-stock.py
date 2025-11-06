class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # suppose initial me min_price jho hai vho
        min_price=prices[0]
        #max_profit initial me 0 
        max_profit=0
        # here we are checking each price 
        for price in prices:
            #price to be smallest 
            if price<min_price:
                min_price=price
            #profit la calculation     
            curr_profit=price-min_price
            if curr_profit>max_profit:
                max_profit=curr_profit
        return max_profit



        