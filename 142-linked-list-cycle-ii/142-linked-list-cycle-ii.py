# mrasimzahid.github.io

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        seek = dict()
        # pos
        while head:
            if head in seek:
                return head
            seek[head] = True            
            # seek[head]
            head = head.next
        return None