#https://leetcode.com/problems/add-two-numbers-ii/
#https://github.com/MrAsimZahid
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_str = ""
        while l1:
            l1_str = l1_str + str(l1.val)
            l1 = l1.next
        l2_str = ""
        while l2:
            l2_str = l2_str + str(l2.val)
            l2 = l2.next
        
        l3_sum = str(int(l1_str) + int(l2_str))
        
        l3 = ListNode(int(l3_sum[0]))
        
        head = l3
        
        for i in range(1, len(l3_sum)):
            head.next = ListNode(int(l3_sum[i]))
            head = head.next
        return l3
