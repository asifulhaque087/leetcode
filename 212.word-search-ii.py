#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in  word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. have to add all the words to a prefix tree
        # 2. dfs to the board and check if any word exists
        
        # adding all word to a perfix tree
        root = TrieNode()
        for w in words:
            root.addWord(w)

        # print(vars(root))
        ROWS , COLS = len(board) , len(board[0])

        # vis = [[False for j in range(C)] for i in range(R)]
        res, visit= set(), set()

        # def isValid(row, col, node):
            
        #     if (row < 0 or col < 0 or row >= R or col >= C):
        #         return False

        #     if  board[row][col] in node.childrens:
        #         return False
        
        #     if (vis[row][col]):
        #         return False

        #     return True


        def dfs(r, c, node, word):


            # if not isValid(row,col,node):
            #     return 

            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] not in node.children):
                return 


            # vis[row][col] = True
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)


            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)

            # vis[row][col] = False
            visit.remove((r,c))



        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")


        return list(res)

        
# @lc code=end

