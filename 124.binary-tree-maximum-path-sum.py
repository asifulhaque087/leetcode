#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(root):
            nonlocal res
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            l = max(l, 0)
            r = max(r, 0)


            # splitting 
            res = max(res, root.val + l + r)

            # without splitting 
            return root.val + max(l,r)
        dfs(root)
        return res
            
        
# @lc code=end

