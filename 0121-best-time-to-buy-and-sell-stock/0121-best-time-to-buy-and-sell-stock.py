class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap=prices[0]
        profit=0
        for i in prices:
            if i<cheap:
                cheap=i
            else:
                profit=max(profit,i-cheap)
        return profit