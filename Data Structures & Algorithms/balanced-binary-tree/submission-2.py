# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]


        
    def dfs(self, root):
        if not root:
            return [True, 0]
        
        ball, Dleft = self.dfs(root.left)
        balr, Dright = self.dfs(root.right)

        balanced = ball and balr and abs(Dleft - Dright) <= 1
        
        return [balanced, 1 + max(Dleft, Dright)]