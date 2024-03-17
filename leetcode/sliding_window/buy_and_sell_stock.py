class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            r += 1

        return maxProfit