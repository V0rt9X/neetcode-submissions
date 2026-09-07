# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        return self.dfs(root, root.val)

    def dfs(self, root, val):
        if not root:
            return 0

        if root.val >= val:
            return 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val)
        else:
            return 0 + self.dfs(root.left, val) + self.dfs(root.right, val)
        

