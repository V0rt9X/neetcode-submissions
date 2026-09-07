class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {src: [] for src in range(n)}

        for ed1, ed2 in edges:
            adj[ed1].append(ed2)
            adj[ed2].append(ed1)
        
        visited = set()
        def dfs(src, prev):
            if src in visited:
                return False
            
            visited.add(src)

            for nei in adj[src]:
                if nei == prev:
                    continue

                if not dfs(nei, src):
                    return False
            
            return True
        
        res = dfs(0, -1)
        return res if len(visited) == n else False
        
