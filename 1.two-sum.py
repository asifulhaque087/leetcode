#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            need = target - nums[i]

            if need in map:
                return [map[need], i]
            map[nums[i]] = i
            






        
# @lc code=end

