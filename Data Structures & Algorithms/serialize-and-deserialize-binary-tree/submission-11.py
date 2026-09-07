# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = []

        def dfs(root):
            if not root:
                serialized.append("N")
                return
            
            serialized.append(str(root.val))

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        return ",".join(serialized)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        iterator = iter(data)

        def dfs():
            c = next(iterator)

            if c == "N":
                return None
            
            node = TreeNode(int(c), dfs(), dfs())

            return node
        
        return dfs()