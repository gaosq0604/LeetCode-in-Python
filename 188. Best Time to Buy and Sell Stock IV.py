class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        def maxProfitKInf(prices):
            max_profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    max_profit += prices[i] - prices[i-1]
            return max_profit

        if k == 0 or not prices:
            return 0
        
        n = len(prices)

        # k is considered as infinite here
        if k >= n / 2:
            return maxProfitKInf(prices)

        # buy: the most amount you can make at most j transactions with item 0 to 1 with possible buy or holding
        # sell: the most amount you can make at most j transactions with item 0 to 1 with possible sell or no holding
        buy, sell = [float('-inf')] * (k+1), [0] * (k+1)
        for i in range(n):
            for j in range(1, k+1):
                buy[j] = max(buy[j], sell[j-1] - prices[i])
                sell[j] = max(sell[j], buy[j] + prices[i])
        return sell[k]