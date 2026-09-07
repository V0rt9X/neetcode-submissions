# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]
            
            Dleft = dfs(root.left)
            Dright = dfs(root.right)

            balanced = Dleft[0] and Dright[0] and abs(Dleft[1] - Dright[1]) <= 1

            return [balanced, max(Dleft[1], Dright[1]) + 1]
        
        return dfs(root)[0]