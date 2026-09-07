# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftD = self.dfs(root.left)
        rightD = self.dfs(root.right)

        balanced = abs(rightD - leftD) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

        if not balanced:
            return False
        
        return True

        
    def dfs(self, root):
        if not root:
            return 0
            
        return 1 + max(self.dfs(root.left), self.dfs(root.right))