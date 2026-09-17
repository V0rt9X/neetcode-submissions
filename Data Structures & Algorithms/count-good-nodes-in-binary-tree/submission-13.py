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
            
            leftG = dfs(root.left, max(root.val, prev))
            rightG = dfs(root.right, max(root.val, prev))

            if root.val < prev:
                return 0 + leftG + rightG
            
            return 1 + leftG + rightG
        
        return dfs(root, root.val)

        # t O(n) s O(n)