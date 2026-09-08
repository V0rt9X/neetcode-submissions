"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clones = {}

        def clone(root):
            if root in clones:
                return clones[root]

            copy = Node(root.val)
            clones[root] = copy

            for nei in root.neighbors:
                copy.neighbors.append(clone(nei))
            
            return copy
        
        return clone(node)