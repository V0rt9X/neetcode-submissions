# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = collections.deque([root])
        res = []

        while q:
            rightS = None
            for _ in range(len(q)):
                curr = q.popleft()
                rightS = curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
            res.append(rightS)
        
        return res

