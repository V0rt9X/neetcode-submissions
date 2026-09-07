# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, prev):
            if not root:
                return 0
            
            leftG = dfs(root.left, max(prev, root.val))
            rightG = dfs(root.right, max(prev, root.val))

            if root.val >= prev:
                return leftG + rightG + 1
            else:
                return leftG + rightG
            
        
        return dfs(root, float("-inf"))