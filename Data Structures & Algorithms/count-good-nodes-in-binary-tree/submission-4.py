# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, prevMax):
            if not root:
                return 0
            
            res = 1 if root.val >= prevMax else 0
            prevMax = max(prevMax, root.val)

            res += dfs(root.left, prevMax)
            res += dfs(root.right, prevMax)

            return res
        
        return dfs(root, root.val)