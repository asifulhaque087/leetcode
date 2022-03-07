

def productExSelf(nums):
    res = [1] * len(nums)

    pre_fix = 1

    for i in range(len(nums)):
        res[i] =  pre_fix
        pre_fix = pre_fix*nums[i]

    post_fix = 1
    for i in range(len(nums)-1, -1 , -1):
        res[i] = res[i]*post_fix
        post_fix = post_fix*nums[i]
    return res


#prefix ber korse, r akane kno number er prefix mane oi number er age porjonto number er gun, r atake store kora hoi current number er niche


#tarpor postfix a kno number er er porer number teke sesh number porjonto gun foler sateh prefix er gun e ans


# arr = [1,2,3,4]

# print(productExSelf(arr))



def maxSubArr(nums):
    m = nums[0]
    total = 0
    for num in nums:
        if total < 0:
            total = 0
        total+=num

        m = max(m, total)

    return m

# protibar add houar somoi max value er sathe compare kora hoi. 

arr = [-2, 1,-3, 4, -1, 2, 1, -5, 4]

# print(maxSubArr(arr))








def climbing_stairs(n):
    if n == 0:
        return 1
    if n < 0 :
        return 0

    res = 0

    res+= climbing_stairs(n-1)  
    res+= climbing_stairs(n-2)
    return res
    

# print(climbing_stairs(4))
total = 5
arr = [1,2,5]

# total = 100
# arr = [3,5,7,8,9,10,11]

def coinEx(amount, coins):
    memo = {}

    def helper(amount , coins, index):
        if amount == 0:
            return 1
        if amount < 0 or index == len(coins):
            return 0


        key = str(amount) + "mridul" + str(index)
        if key in memo:
            return memo[key]


        res = 0
        for i in range(index,len(coins)):
            if amount>= coins[i]:
                res+=helper(amount-coins[i], coins, i)
        memo[key] = res

        return res


    return helper(amount, coins, 0)

# print(coinEx(total,arr))


# def coinEx(amount, coins):
#     memo = {}

#     def helper(amount , coins, index):
#         if amount == 0:
#             return 1
#         if amount < 0 or index == len(coins):
#             return 0


#         key = str(amount) + "mridul" + str(index)

#         if key in memo:
#             return memo[key]


#         res = 0
#         i = index
#         while i < len(coins):
#             if amount>= coins[i]:
#                 res+=helper(amount-coins[i], coins, i)
#             i+=1
            
#         memo[key] = res

#         return res

#     # print(memo)

#     return helper(amount, coins, 0)-1

# print(coinEx(total,arr))


def fac(n):
    if n == 1 or n == 0:
        return 1
    res = 0

    print(n)
    res+=  n * fac(n-1)
    return res

# print(fac(3))

# print(18/0)

arr = [10,9,2,5,3,7,101,18]


def lis(nums):
    def helper(i):
        ans = 1
        j = 0
        while j < i:
            if nums[j]<nums[i]:
                ans=max(ans, helper(j)+1)
            j+=1
        return ans


    ans = 0

    for i in range(len(nums)):
        ans = max(ans, helper(i))
    return ans





# print(lis(arr))


# s = "leetcode"
# wordDict = ["leet","code"]

# s = "applepenapple"
# wordDict=["apple","pen"]

# s = "bccdbacdbdacddabbaaaadababadad"
# wordDict=["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"]


# def word_break(s, wordDict):
#     map = {}
#     def helper(i):
#         if i == len(s):
#             return True
        
#         if i > len(s):
#             return False
#         if i in map: 
#             return map[i]

#         res = False
#         for word in wordDict:
#             word_length = len(word)
#             # print("word is ",word)
#             # print("substring is ",s[i:][:word_length])
#             if word == s[i:][:word_length]:
#                 if helper(i+word_length):
#                     res = True
                
#         pass
#         map[i] = res
#         return res
    
#     return helper(0)

# print(word_break(s, wordDict))

a = [2,3,6,7]
t = 7

def combinationSum(candidates, target):
    res = []

    def helper(total,rarr, index):

        if total == target:
            res.append(rarr)

        if total > target:
            return

        for i in range(index,len(candidates)):
            if candidates[i] <= target:
                helper(total+candidates[i], rarr+[candidates[i]], i)

    helper(0,[],0)

    return res 


# print(combinationSum(a,t))

# print([3]+[2])

# nums = [1,2,3,1]
# for i in range(0,len(nums),1):
#     print(nums[i])

n = [1,2,3,1]
 
# n = [2,7,9,3,1]

def rob(nums):

    def helper(index,step, depth, ar):
        if depth == len(nums)-1:
            # print("depth is ", depth)
            # print("nums is", nums[index])
            # return nums[index]
            print(ar, sum(ar))
            return sum(ar)

        s = 0

        if not (index % 2 == 0):
            s = 1

        res = 0
        for i in range(s,len(nums),step):
            # print(nums[i])
            # if not (i == index):
            r = helper(i, 2, depth+1, ar+[nums[i]])
            # print("total is ", r)
            res = max(res, r)

        return res



    return helper(0,1,1,[])



# print(rob(n))

coins = [1,2,5]

amount = 11

coins = [1,2]
amount = 3

def coinChange(coins, amount):

    dp = {}
    def helper(amount, branch):

        if amount == 0:
            return 0

        if amount in dp:
            return dp[amount]
        
        res = float("+inf")
        for coin in coins:
            if amount - coin >= 0:
                res = min(res, helper(amount - coin, branch + [coin])+1)

        dp[amount] = res
        return res

    return helper(amount,[])



# print(coinChange(coins, amount))


s = "leetcode"
w = "leet"

# print(s[4:][:len(w)])
# print(s[4:][:3])
# print(s[4:])


# ami jei rokom chai ai rokom recursion banano lagbe









class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):

        newNode = Node(val) 

        if self.head == None:
            self.head =  newNode
        else:
            tempt = self.head
            while tempt:
                lastNode = tempt
                tempt = tempt.next
            lastNode.next = newNode

    def appendArr(self, arr):
        for item in arr:
            self.append(item)
    
    def returnHead(self):
        return self.head


    def printLinkList(self):

        printVal = self.head
        while printVal is not None:
            print(printVal.val)
            printVal = printVal.next




ll = LinkedList()

ll.appendArr(range(10))

# ll.printLinkList()

print(ll.returnHead().val)


# print()