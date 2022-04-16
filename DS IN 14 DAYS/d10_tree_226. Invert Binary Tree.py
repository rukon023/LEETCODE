# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, node):
        if node:
            tmp_node = node.left
            node.left = node.right
            node.right = tmp_node
            self.dfs(node.left)
            self.dfs(node.right)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        self.dfs(root)
        return root
    