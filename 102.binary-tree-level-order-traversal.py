#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # declare a que. 
        # in first loop insert all node of a specific level
        # second loop delete all the node of previous level and add all node of current level

        # declare a que. 
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            level = []

            for i in range(len(q)):
                # delete all the node of previous level
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    # inserting  all node of a specific level
                    q.append(node.left)
                    q.append(node.right)
                
            if level:
                res.append(level)

        return res


        
# @lc code=end

