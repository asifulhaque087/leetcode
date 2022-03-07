#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1 . iterate 2 list at a time and merge into one and append it to a new list. 
        # 2 . then assign lists = mergedlsit 
        # 3. continue this process till 1 list left

        if not lists or len(lists) == 0:
            return None
        # continuing the process
        while len(lists) > 1:
            mergedList = []
            # iterate over 2 list at a time
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                # after merging two list into one appending to mergelist
                mergedList.append(self.mergeList(l1, l2))
            # assiging lists = mergedList
            lists = mergedList
        return lists[0]

    def mergeList(self, l1, l2):
        dummy  = ListNode()
        tail = dummy

        while l1 and l2: 
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else: 
                tail.next  = l2
                l2 = l2.next
            tail = tail.next
        
        if l1: 
            tail.next = l1
        if l2: 
            tail.next = l2

        return dummy.next


        
# @lc code=end

