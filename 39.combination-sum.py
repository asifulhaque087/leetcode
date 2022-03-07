#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(index, target, arr):
            if target == 0:
                res.append(arr)

            for i in range(index, len(candidates)):
                if target - candidates[i] >= 0:
                    helper(i, target -  candidates[i], arr+[candidates[i]])
        helper(0, target, [])

        return res

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         def func(index, target,arr):
#             if target == 0:
#                 res.append(arr)

#             for i in range(index,len(candidates)):
#                 if target - candidates[i] >= 0:
#                     func(i, target-candidates[i], arr+[candidates[i]])
            
#         func(0, target, [])
#         return res
            

        
# @lc code=end

