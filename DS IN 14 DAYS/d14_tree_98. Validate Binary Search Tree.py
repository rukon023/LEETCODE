# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
https://leetcode.com/problems/validate-binary-search-tree/discuss/1743459/Very-easy-python-recursive-solution.-Beat-84.66"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        left, right = float('-inf'), float('inf')
        def inorder(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            check_left = inorder(node.left, left, node.val)
            check_right = inorder(node.right, node.val, right)
            
            return check_left and check_right
            
        return inorder(root, left, right)