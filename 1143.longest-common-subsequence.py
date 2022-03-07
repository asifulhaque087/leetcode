#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def helper(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            
            key = str(i)+"mridul"+str(j)

            if key in dp:
                return dp[key]

            op1 = 0

            if text1[i] == text2[j]:
                op1 += 1+helper(i+1, j+1)

            op2 = helper(i,j+1)
            op3 = helper(i+1,j)

            res = max(op1,op2, op3)
            dp[key] = res
            return res

        return helper(0,0)
            
                




# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp = {}
#         def func(i,j):
#             if i == len(text1) or j == len(text2):
#                 return 0

#             key = str(i)+"mridul"+str(j)
#             if key in dp:
#                 return dp[key]

#             op1 = 0
#             if text1[i] == text2[j]:
#                 op1+=func(i+1,j+1)+1
            
#             op2 = func(i,j+1)
#             op3 = func(i+1,j)

#             res = max(op1,op2,op3)

#             dp[key] = res
#             return res

#         return func(0,0)


        
# @lc code=end

