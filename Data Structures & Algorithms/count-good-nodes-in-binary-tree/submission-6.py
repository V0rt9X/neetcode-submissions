# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(root, pastM):
            if not root:
                return 
            
            self.res += 1 if pastM <= root.val else 0
            pastM = max(pastM, root.val)

            dfs(root.left, pastM)
            dfs(root.right, pastM)

            return
        
        dfs(root, root.val)

        return self.res    
            