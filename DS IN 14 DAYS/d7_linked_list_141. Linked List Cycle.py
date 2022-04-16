# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        ##################### Soln 2: using 2 pointers & O(1) space ###########
        slow, fast = head, head
        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is None: 
                break
            else: 
                fast = fast.next
            if slow == fast:
                return True 
        return False
        
        
        ##################### Soln 1: Using Hashmap ###########
        # check_dict = {}
        # node = head
        # while node is not None:
        #     if node in check_dict:
        #         return True
        #     else:
        #         check_dict[node] = True
        #     node = node.next