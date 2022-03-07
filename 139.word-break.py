#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def helper(i):
            if i == len(s):
                return True

            if i in dp:
                return dp[i]

            res = False
            for word in wordDict:
                if s[i:][:len(word)] == word:
                    if helper(i+len(word)): res = True

            dp[i] = res
            return res

        return helper(0)



# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         dp = {}
#         def func(i):
#             if i == len(s):
#                 return True

#             if i in dp:
#                 return dp[i]

#             res = False

#             for word in wordDict:
#                 if word == s[i:][:len(word)]:
#                     if func(i+len(word)): res = True

#             dp[i] = res
#             return res

#         return func(0)
        
# @lc code=end

