# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(root):
            if not root:
                return 0
            
            leftD = dfs(root.left)
            rightD = dfs(root.right)

            self.res = max(self.res, leftD + rightD)

            return 1 + max(leftD, rightD)
        
        dfs(root)

        return self.res