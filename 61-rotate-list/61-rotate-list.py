# mrasimzahid.github.io

# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        last_node = head
        len_count = 1
        while last_node.next:
            last_node = last_node.next
            len_count += 1
            
        k = k % len_count 
        last_node.next = head
        
        temp_node = head
        for _ in range(len_count - k -1):
            temp_node = temp_node.next
            
        ans = temp_node.next
        temp_node.next = None
        return ans
    