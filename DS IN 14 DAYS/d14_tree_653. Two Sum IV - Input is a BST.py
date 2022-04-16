# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ######## Soln 2: Iterative ########
        
        ######## Soln 1: Recursion ########
        def check_bst(node, k, hash_map):
            if not node:
                return False
            if node.val in hash_map:
                return hash_map[node.val]
            else:
                #node.val not in hash_map:
                hash_map[k - node.val] = True
            #ans = check_bst(node.left, k, hash_map) or check_bst(node.right, k, hash_map)
            #print("final", ans)
            return check_bst(node.left, k, hash_map) or check_bst(node.right, k, hash_map)
        hash_map = {}    
        return check_bst(root, k, hash_map)