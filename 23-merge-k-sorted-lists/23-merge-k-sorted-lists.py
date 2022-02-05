# mrasimzahid.github.io

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = []
        dummy = ListNode(None)
        current = dummy
        for each_list in lists:
            while each_list:
                result.append(each_list.val)
                each_list = each_list.next
        for each in sorted(result):
            current.next = ListNode(each)
            current = current.next
        return dummy.next
        