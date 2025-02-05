class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        buy = prices[0]
        for i in range(1, len(prices)):
            # if see a low price, then consider buying it unless there's a lower price
            # if see high price, check the difference see if its high then do transaction

            if prices[i] < buy:
                buy = prices[i]

            profit = prices[i] - buy


            
            max_profit = max(max_profit, profit)

        return max_profit


            

        