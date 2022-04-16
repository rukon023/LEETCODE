# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val==targetSum
        
        def preorder(node, cur_sum, targetSum):
            if not node:
                return False
            cur_sum += node.val
            print(node.val, cur_sum)
            if cur_sum==targetSum and node.left==None and node.right==None:
                return True
            return preorder(node.left, cur_sum, targetSum) or preorder(node.right, cur_sum, targetSum)
        
        return preorder(root, 0, targetSum)
    
            ########### Soln 1 ##############
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
#         if not root.left and not root.right:
#             return root.val==targetSum
        
#         global flag
#         flag = False
#         def dfs(node, summ):
#             global flag
#             if not node:
#                 return 
#             if flag:
#                 return  
#             summ += node.val
#             print(node.val, summ)
#             if (summ==targetSum) and (not node.left) and (not node.right):
#                 flag = True
#             dfs(node.left, summ)
#             dfs(node.right, summ)
#         dfs(root, 0)
#         return flag
