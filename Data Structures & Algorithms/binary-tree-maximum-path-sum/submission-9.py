# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            left = left if left > 0 else 0
            right = right if right > 0 else 0

            self.res = max(self.res, left + right + root.val)

            return root.val + max(left, right)
        
        dfs(root)
        return self.res