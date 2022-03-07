#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        l,r = 0,1
        while r<len(prices):
            if prices[r]> prices[l]:
                profit = max(profit, prices[r]-prices[l])
            else:
                l = r
            r+=1
        return profit
            





# jodi agee e r = 1 nei, tarporeo r < len(prices) dile kno error asbe na, r = 2nd value houa hotto

# @lc code=end

