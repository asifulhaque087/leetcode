#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = nums[0]
        total = 0
        for num in nums:
            if total < 0:
                total = 0
            total+=num
            max_total = max(max_total, total)
        return max_total



        
# @lc code=end

