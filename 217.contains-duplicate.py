#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = set()
        for num in nums:
            if num in map:
                return True
            map.add(num)
        
# @lc code=end

