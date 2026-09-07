# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                rightS = node
                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)
            if rightS:
                res.append(rightS.val)
        
        return res