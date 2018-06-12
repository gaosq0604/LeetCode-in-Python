class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice, maxprofit = float('inf'), 0
        for price in prices:
            profit = price-minprice
            maxprofit = max(profit, maxprofit)
            minprice = min(price, minprice)
        return maxprofit