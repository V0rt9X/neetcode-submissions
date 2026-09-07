# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        
        def dfs(root):

            if p.val <= root.val <= q.val:
                return root
            elif p.val > root.val and q.val > root.val:
                return dfs(root.right)
            else:
                return dfs(root.left)
        
        return dfs(root)
