class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # track the lowest price have have seen so far 
        # that is the best day to buy for anything in the future
        # also tracking the best profit we have seen so far 
        best = 0
        mn = 101
        for i in range(len(prices)):
            if prices[i] < mn:
                mn = prices[i]
            profit = prices[i] - mn
            best = max(profit, best)
        return best 

            
        