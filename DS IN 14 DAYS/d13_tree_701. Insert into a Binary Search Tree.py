# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        #### Soln 2 ####
        if not root:
            new = TreeNode(val)
            return new
        
        node, prev = root, TreeNode() 
        while node:
            prev = node
            if val < node.val:
                node = node.left       
            else:
                node = node.right
        
        new = TreeNode(val)
        if prev.val > val:
            prev.left = new
        else:
            prev.right = new
            
        return root
        
        ################# Soln 1 #########
#         if not root:
#             newNode = TreeNode(val, None, None)
#             return newNode
        
#         node = root
#         while node:
#             if node.val < val:
#                 if node.right:
#                     node = node.right
#                 else: 
#                     newNode = TreeNode(val, None, None)
#                     node.right = newNode
#                     return root
#             elif node.val > val:
#                 if node.left:
#                     node = node.left
#                 else:
#                     newNode = TreeNode(val, None, None)
#                     node.left = newNode
#                     return root