#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    

    def climbStairs(self, n: int) -> int:
        dp = {}

        def func(n):
            if n == 0: return 1

            if n in dp:
                return dp[n]
        
            res = 0
            res+=func(n-1)
            if n-2 >= 0:
                res+=func(n-2)

            dp[n] = res
            return res
        
        return func(n)



            

        
        
        

        
# @lc code=end