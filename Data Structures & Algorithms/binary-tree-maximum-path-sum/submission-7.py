# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def dfs(root):
            if not root:
                return 0
        
            leftP = dfs(root.left)
            rightP = dfs(root.right)

            leftP = leftP if leftP > 0 else 0
            rightP = rightP if rightP > 0 else 0

            self.res = max(self.res, root.val + leftP + rightP)

            return root.val + max(leftP, rightP)
        
        dfs(root)
        return self.res

