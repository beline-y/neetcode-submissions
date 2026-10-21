class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_delta = 0
        minp = prices[0]

        for sell in prices:
            max_delta = max(max_delta, sell - minp)
            minp = min(minp, sell)
        return max_delta