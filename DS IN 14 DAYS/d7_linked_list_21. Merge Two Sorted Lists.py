# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        head = ListNode()
        tmp_node = head
        while node1 is not None and node2 is not None:
            if node1.val <= node2.val:
                tmp_node.next = node1
                node1 = node1.next
            else:
                tmp_node.next = node2
                node2 = node2.next
            tmp_node = tmp_node.next
            
        if node1 is not None:
            tmp_node.next = node1
        if node2 is not None:
            tmp_node.next = node2
        return head.next