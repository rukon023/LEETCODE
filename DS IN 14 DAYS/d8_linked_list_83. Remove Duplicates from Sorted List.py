# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = head
        curr = head
        
        while curr:
            if curr.val != prev.val:
                prev.next = curr
                prev = prev.next
            curr = curr.next
        
        if prev:
            prev.next = None
        return head

    
        ###################### Soln 1 ##################
        # curr = head
        # while curr:
        #     nextt = curr.next
        #     if nextt:
        #         while nextt.val == curr.val:
        #             nextt = nextt.next
        #             if nextt is None:
        #                 break
        #         curr.next = nextt
        #     curr = nextt
        # return head