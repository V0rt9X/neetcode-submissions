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
            
            leftS = dfs(root.left)
            rightS = dfs(root.right)
            leftS = max(0, leftS)
            rightS = max(0, rightS)

            res[0] = max(res[0], leftS + rightS + root.val)

            return root.val + max(leftS, rightS)
        
        dfs(root)
        return res[0]