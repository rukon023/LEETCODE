# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def checkSymmetry(self, left_tree, right_tree):
        if not left_tree and not right_tree:
            return True
        elif left_tree and not right_tree:
            return False
        elif not left_tree and right_tree:
            return False
        elif left_tree.val != right_tree.val:
            return False
        
        mirror1 = self.checkSymmetry(left_tree.left, right_tree.right)
        mirror2 = self.checkSymmetry(left_tree.right, right_tree.left)
        
        return mirror1 and mirror2
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.checkSymmetry(root.left, root.right)
    
    # def leftDFS(self, node, ans):
    #     if node:
    #         ans.append(node.val)
    #         self.leftDFS(node.left, ans)
    #         self.leftDFS(node.right, ans)
    #     return ans
    # def rightDFS(self, node, ans):
    #     if node:
    #         ans.append(node.val)
    #         self.rightDFS(node.right, ans)
    #         self.rightDFS(node.left, ans)
    #     return ans