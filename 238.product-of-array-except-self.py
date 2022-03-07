#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        print(res)

        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = post*res[i]
            post *= nums[i]
        return res


        
# @lc code=end

