# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(leftS, root, rightS):
            if not root:
                return True
            
            if leftS < root.val < rightS:
                return dfs(leftS, root.left, root.val) and dfs(root.val, root.right, rightS)
            else:
                return False
        
        return dfs(float("-inf"), root, float("inf"))