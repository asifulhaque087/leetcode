#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = {}

        def helper(i):

            if i == len(s):
                return 1
            
            # if s[i] =="0":
            #     return 0

            if i == len(s) - 1:
                return 1
            if i in dp:
                return dp[i]

            way1= helper(i+1)
            way2 = 0
            # if int(s[i:][:i+2]) <= 26:
            if int(s[i:i+2]) <= 26:
                way2 = helper(i+2)


            # return way1+way2
            dp[i] = way1+way2
            return way1 + way2


        return helper(0)
        
# @lc code=end

