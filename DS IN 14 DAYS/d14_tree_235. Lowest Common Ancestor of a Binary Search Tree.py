# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/1741299/Two-Python-Solution-(Recursion+Iteration)-Easy-to-Understand
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #### Soln 2: Recursive Method ###
        if p==root or q==root:
            return root
        node = root
        def helper(node, p, q):
            # p is in the left & q is in the right or vice versa, root is ans
            if (p.val <= node.val and q.val >= node.val) or (q.val <= node.val and p.val >= node.val):
                return node
            # p & q are in the left subtree
            elif p.val <= node.val and q.val <= node.val:
                node = helper(node.left, p, q)
            # p & q are in the right subtree
            elif p.val >= node.val and q.val >= node.val:
                node = helper(node.right, p, q)
            return node
        return helper(node, p, q)            
        
        ### Soln 1: Iterative Method ###
        # if p==root or q==root:
        #     return root
        # while root:
        #     ## p & q are both in the left subtree
        #     if p.val < root.val and q.val < root.val:
        #         root = root.left
        #     ## p & q are both in the right subtree
        #     elif p.val > root.val and q.val > root.val:
        #         root = root.right
        #     else:
        #         return root