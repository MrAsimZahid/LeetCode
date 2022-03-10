# mrasimzahid.github.io

# Technique: String conversion
# Technique2: Carry
# Technique3: Base calculate

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = ""
        l2_str = ""
        while l1:
            l1_str += str(l1.val)
            l1 = l1.next

        while l2:
            l2_str += str(l2.val)
            l2 = l2.next

        l1_int = int(l1_str[::-1])
        l2_int = int(l2_str[::-1])
        res = l1_int + l2_int
        dummy = curr = ListNode(-1)
        for integer in str(res)[::-1]:
            curr.next = ListNode(integer)
            curr = curr.next
        return dummy.next