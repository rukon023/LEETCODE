# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #################### Soln 2: Using Recursion ############
        if not root:
            return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        return max(leftDepth, rightDepth) + 1
        
        
        #################### Soln 1: Using Iteration #############
        # if not root:
        #     return 0
        # queue = deque([root])
        # level = 0
        # while queue:
        #     level += 1
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return level