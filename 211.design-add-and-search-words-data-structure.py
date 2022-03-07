#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#


# @lc code=start

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur  = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

        

    def search(self, word: str) -> bool:
        # loop through every char in word if all are available in trie then return True
        # else return  False

        # if char == "." make recursion in every path (a:{}, b:{},....)

        def dfs(j,root):
            cur = root        

            for i in range(j,len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child): return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.isWord

        return dfs(0, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

