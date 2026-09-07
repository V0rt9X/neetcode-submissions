# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(current):
            if not current:
                return 0
            
            Dleft = dfs(current.left)
            Dright = dfs(current.right)

            self.res = max(self.res, Dleft + Dright)

            return 1 + max(Dleft, Dright)
        
        dfs(root)

        return self.res
