# mrasimzahid.github.io

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = {}
        while head:
            if store.get(head.val):
                store[head.val] = store.get(head.val) + 1                
            else:
                store[head.val] = 1
            head = head.next
        
        dummy = curr = ListNode(-1)
        for val in store:
            if store.get(val) == 1:
                curr.next = ListNode(val)
                curr = curr.next
        return dummy.next
#         temp = []
#         while head.next:
#             temp.append(head.val)
#         return temp
#         curr.next = head
#         curr = curr.next
#         while curr.next:
#             if curr.val == curr.next.val:
#                 curr.next = curr.next.next
#             else:
#                 curr = curr.next
                
#         return dummy.next