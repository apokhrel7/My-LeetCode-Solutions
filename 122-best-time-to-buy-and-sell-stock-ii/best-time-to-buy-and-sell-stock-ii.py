class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # if you notice previous price was cheaper, sell buy it on that previous day and sell immediately
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit