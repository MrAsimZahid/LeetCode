# mrasimzahid.github.io

# Technique: Store values and nodes in a list of tuples,
# and then access data and delete after using it.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.cache = []
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        pseudo_head = head
        while pseudo_head:
            self.cache.append((pseudo_head.val, pseudo_head))
            pseudo_head = pseudo_head.next
        sort_res = sorted(self.cache, key=lambda x : x[0])
        dummy = ListNode(-1)
        curr = dummy.next = sort_res[0][1]
        for num in sort_res[1:]:
            node = num[1]
            node.next = None
            curr.next = node
            curr = curr.next
        return dummy.next

