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
                return (0, True)
        
            leftD = dfs(root.left)
            rightD = dfs(root.right)

            balanced = abs(rightD[0] - leftD[0]) <= 1 and leftD[1] and rightD[1]

            if not balanced:
                return (-1, False)
            
            return (1 + max(leftD[0], rightD[0]), balanced)
        
        return dfs(root)[1]