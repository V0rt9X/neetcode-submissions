class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency = { ed: [] for ed in range(n)}

        visited = set()
        for ed1, ed2 in edges:
            adjacency[ed1].append(ed2)
            adjacency[ed2].append(ed1)
        
        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)

            for nei in adjacency[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            
            return True
        
        return dfs(0, -1) and n == len(visited)
