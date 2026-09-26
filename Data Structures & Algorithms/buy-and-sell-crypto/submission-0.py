class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        sell=len(prices)-1
        buy = sell-1
        while buy>-1:
            if prices[buy]>prices[sell]:
                sell=buy
            max_profit=max(max_profit, prices[sell]-prices[buy])
            buy-=1
        return max_profit