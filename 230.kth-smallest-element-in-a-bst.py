#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # n for tracking so that it is == k then we are gonna have answer
        # iterate over tree and go left as it is possible and add them to the stack , like inorder traversal. 
        # when pop back to parent remove parent from stack then increment n 
        # if n not equal to k then go right

        n = 0
        stack = []
        cur = root

        while cur or stack:
            # getting left as far as possible
            while cur:
                stack.append(cur)
                cur = cur.left

            # popping from stack means visiting the parent
            cur = stack.pop()

            # incrementing n so that we can check with k 
            n += 1
            if n == k :
                return cur.val
            
            # not n == k then going right 
            cur = cur.right
            

        
# @lc code=end

