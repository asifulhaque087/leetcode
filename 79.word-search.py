#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        R = len(board)
        C = len(board[0])

        vis = [[False for j in range(C)] for i in range(R)]

        path = set()

        def isValid(row, col, i):
            
            if (row < 0 or col < 0 or row >= R or col >= C):
                return False

            if not (word[i] == board[row][col]):
                return False
        
            if (vis[row][col]):
                return False

            return True


        def dfs(row, col, i):

            if i == len(word):
                return True

            if not isValid(row,col,i):
                return False

            vis[row][col] = True

            res = (dfs(row-1, col, i+1) or dfs(row, col+1, i+1) or dfs(row+1, col, i+1) or dfs(row, col-1, i+1))

            vis[row][col] = False

            return res


        for r in range(R):
            for c in range(C):
                if dfs(r,c,0):return True
        return False
                


        
# @lc code=end

