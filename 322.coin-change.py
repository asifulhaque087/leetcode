#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def func(amount):
            if amount == 0:
                return 0

            if amount in dp: return dp[amount]

            res = float("+inf")

            for coin in coins:
                    if amount - coin >= 0:
                        res = min(res, 1+func(amount-coin))

            dp[amount] = res
            return res

        
        res = func(amount)
        return -1 if res == float("+inf") else res
        
# @lc code=end



# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = {}

#         def func(amount):

#             if amount == 0:
#                 return 0

#             if amount in dp:
#                 return dp[amount]

#             res = float("+inf")

#             for coin in coins:
#                 if not (amount - coin < 0):
#                     res = min(res,func(amount - coin) + 1)

#             dp[amount] = res

#             return res
            

            
        
#         res = func(amount)
#         print("res is ", res)

#         return -1 if res == float("+inf") else res
        
# @lc code=end


