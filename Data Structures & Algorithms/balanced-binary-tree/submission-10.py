# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return (True, 0)
            
            leftD = dfs(root.left)
            rightD = dfs(root.right)

            balanced = leftD[0] and rightD[0] and abs(leftD[1] - rightD[1]) <= 1

            return (balanced, 1 + max(leftD[1], rightD[1]))
        
        return dfs(root)[0]