# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head
        
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        return prev
        ##################### Soln 1 ##############
#         if head is None:
#             return head
        
#         node = head.next
#         new_head = head
#         new_head.next = None
#         while node:
#             tmp = node
#             node = node.next
#             tmp.next = head
#             head = tmp
#         return head