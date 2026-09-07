# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, leftS, rightS):
            if not root:
                return True
            
            left = dfs(root.left, leftS, root.val)
            right = dfs(root.right, root.val, rightS)

            if leftS < root.val < rightS:
                return left and right
            else:
                return False
        
        return dfs(root, float("-inf"), float("inf"))