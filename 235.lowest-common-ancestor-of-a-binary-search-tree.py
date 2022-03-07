#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # answer would be split node

        # if both value are smaller than cur value the go left
        # if both value are bigger than cur value then go right
        # otherwise there is a split that means this is the ans

        cur = root 

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right

            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left

            else: 
                return cur
        
# @lc code=end

