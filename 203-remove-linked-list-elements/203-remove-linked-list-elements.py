# mrasimzahid.github.io

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # approch 1
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        while node.next != None:
            if node.next.val == val:
                node.next = node.next.next
                # head = head.next
            else:
                node = node.next
        return dummy.next
        
        # approch 2
        # keep a previous pointer