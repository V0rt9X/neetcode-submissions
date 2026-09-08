class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {ed: [] for ed in range(n)}

        for ed1, ed2 in edges:
            adj[ed1].append(ed2)
            adj[ed2].append(ed1)
        
        visited = set()
        cycle = set()

        def dfs(src, prev):
            if src in cycle:
                return False
            if src in visited:
                return True
            
            cycle.add(src)

            for nei in adj[src]:
                if prev == nei:
                    continue
                
                if not dfs(nei, src):
                    return False
                
            cycle.remove(src)
            visited.add(src)
            return True
        res = dfs(0, -1)
        return res if len(visited) == n else False