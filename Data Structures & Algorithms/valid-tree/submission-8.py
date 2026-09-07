class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency = { i: [] for i in range(n) }

        for ed1, ed2 in edges:
            adjacency[ed1].append(ed2)
            adjacency[ed2].append(ed1)
        
        visited = set()

        def dfs(crs, prev):
            if crs in visited:
                return False
            
            visited.add(crs)

            for nei in adjacency[crs]:
                if nei == prev:
                    continue
                
                if not dfs(nei, crs):
                    return False

            return True
        
        res = dfs(0, 0)      
            
        return res if len(visited) == n else False