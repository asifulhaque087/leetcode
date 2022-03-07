#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start

class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = {}

        def helper(i):

            if  i == len(nums):
                return 0
            
            if i in dp:
                return dp[i]

            op1 = nums[i]

            
            if i+2 <= len(nums):
                op1+=helper(i+2)

            op2 = helper(i+1)
            
            res = max(op1, op2)

            dp[i] = res

            return res

        return helper(0)






# class Solution:
#     def rob(self, nums: List[int]) -> int:

#         dp = {}
#         def func(i):

#             if i == len(nums):
#                 return 0
            
#             if i in dp:
#                 return dp[i]

#             op1 = nums[i]

#             if i+2 < len(nums):
#                 op1+=func(i+2)

#             op2 = func(i+1)

#             res = max(op1, op2)
#             dp[i] = res
#             return res
        

            

#         return func(0)


        
# @lc code=end


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         dp = {}
#         def func(i):
#             if i == len(nums)-1:
#                 return nums[i]

#             if i in dp: 
#                 return dp[i]

#             op1 = nums[i]

#             if i+2 < len(nums):
#                 op1 += func(i+2)

#             op2 = func(i+1)
#             res = max(op1, op2)

#             dp[i] = res

#             return res

#         return func(0)