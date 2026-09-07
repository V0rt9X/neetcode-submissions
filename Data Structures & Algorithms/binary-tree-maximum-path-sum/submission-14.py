# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftD = dfs(root.left)
            rightD = dfs(root.right)
            leftD = 0 if leftD < 0 else leftD
            rightD = 0 if rightD < 0 else rightD

            res[0] = max(res[0], leftD + rightD + root.val)

            return root.val + max(leftD, rightD)
        
        dfs(root)
        
        return res[0]