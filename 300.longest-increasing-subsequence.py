#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def func(prev, curr):
            if curr == len(nums):
                return 0

            key = str(prev) + "mridul" + str(curr)

            if key in dp:
                print("dp is ", dp)
                return dp[key]

            op1 = 0

            if prev == -1 or nums[prev]<nums[curr]:
                op1 = 1+func(curr, curr+1) 
            
            op2 = func(prev, curr+1)
            res  = max(op1, op2)
            dp[key] =  res
            return res
        
        return func(-1, 0)
        
# @lc code=end

