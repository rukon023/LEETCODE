# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head and head.val == val:
            head = head.next
        if head is None:
            return head
        
        prev = head
        curr = head.next
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
                
        
        ###################### Soln 1: using extra dummy node #########
        # dummy = ListNode()
        # tail = dummy
        # node = head
        # while node is not None:
        #     if node.val != val:
        #         tail.next = node
        #         tail = tail.next
        #     else:
        #         tail.next = node.next
        #     node = node.next
        # return dummy.next