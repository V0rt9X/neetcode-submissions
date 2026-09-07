# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        r, s = root, subRoot
        if not s:
            return True
        if not r:
            return False
        
        if self.IsSame(r, s):
            return True
        
        return (self.isSubtree(r.left, s) or self.isSubtree(r.right, s))
        
        
    def IsSame(self, r, s):
        if not r and not s:
            return True
        
        if r and s and r.val == s.val:
            return (self.IsSame(r.left, s.left) and self.IsSame(r.right, s.right))
        
        return False