#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # left value will be -infinity  and right value will be +infinity initially
        # recursively going to change r value for l and l value for r

        def dfs(root, l,r):
            if not root:
                return True

            if not (root.val < r and root.val > l):
                return False


            return dfs(root.left, l , root.val) and dfs(root.right, root.val, r)

        return dfs(root, float("-inf"), float("inf"))
        
# @lc code=end

