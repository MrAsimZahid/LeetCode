# mrasimzahid.github.io

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(-1)
        curr.next = head
        
        while curr.next and curr.next.next:
            first = curr.next
            second = first.next
            curr.next = second
            first.next = second.next
            second.next = first
            curr = first
        return dummy.next