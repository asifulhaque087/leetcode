#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.childrens = {}
        self.is_end: False
    
    def addNode(self, word):
        cur = self
        for c in  word:
            if c not in cur.childrens:
                cur.childrens[c] = TrieNode()
            cur = cur.childrens[c]
        cur.is_end = True




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        R = len(board)
        C = len(board[0])

        vis = [[False for j in range(C)] for i in range(R)]

        path = set()

        def isValid(row, col, i, word):
            
            if (row < 0 or col < 0 or row >= R or col >= C):
                return False

            if not (word[i] == board[row][col]):
                return False
        
            if (vis[row][col]):
                return False

            return True


        def dfs(row, col, node, word):

            if i == len(word):
                return True

            if not isValid(row,col,i,word):
                return False

            vis[row][col] = True

            res = (dfs(row-1, col, i+1,word) or dfs(row, col+1, i+1,word) or dfs(row+1, col, i+1,word) or dfs(row, col-1, i+1,word))

            vis[row][col] = False

            return res

        new_list = []

        for w in words:
            for r in range(R):
                for c in range(C):
                    if dfs(r,c,0,w): new_list.append(w)


        return list(set(new_list))

        
# @lc code=end

