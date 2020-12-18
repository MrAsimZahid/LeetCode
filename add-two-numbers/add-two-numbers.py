#https://leetcode.com/problems/add-two-numbers/
#https://github.com/MrAsimZahid
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #convert integrs into string
        l1_str = ""
        while l1:
            l1_str = str(l1.val) + l1_str
            l1 = l1.next
        l2_str = ""
        while l2:
            l2_str = str(l2.val) + l2_str
            l2 = l2.next
        #Sum and convert into string
        l3_sum = str(int(l1_str) + int(l2_str))
        
        #create list node rom reverse side 
        l3 = ListNode(int(l3_sum[-1]))
        #copy node to itr
        itr = l3
        
        #append nodes(reversed values) in linked list
        for i in range(-2, -len(l3_sum) - 1, -1):
            itr.next = ListNode(int(l3_sum[i]))
            itr = itr.next
        #return llist head
        return l3
