# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, pastM):
            if not root:
                return 0
            
            res = 1 if pastM <= root.val else 0
            pastM = max(pastM, root.val)

            res += dfs(root.left, pastM)
            res += dfs(root.right, pastM)

            return res

        return dfs(root, root.val)   
            