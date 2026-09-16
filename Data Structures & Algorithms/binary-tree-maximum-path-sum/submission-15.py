# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            if not root:
                return 0
            
            leftP = dfs(root.left)
            rightP = dfs(root.right)
            leftP = leftP if leftP >= 0 else 0
            rightP = rightP if rightP >= 0 else 0

            nonlocal res

            res = max(res, leftP + rightP + root.val)

            return root.val + max(leftP, rightP)
        
        dfs(root)
        return res
