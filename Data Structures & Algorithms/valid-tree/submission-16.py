class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False # cuts test cases with not valid count of edges to vert

        adj = defaultdict(list) #O(2e)

        for ed1, ed2 in edges: # O(e)
            adj[ed1].append(ed2)
            adj[ed2].append(ed1)
        
        visited = {}
        
        def dfs(src, prev): #O(v)
            if src in visited:
                return visited[src]
            
            visited[src] = False

            for src_nei in adj[src]:
                if src_nei == prev:
                    continue
                
                if not dfs(src_nei, src):
                    return False
            
            visited[src] = True
            return True
        
        res = dfs(0, 0)
        return res if len(visited) == n else False
        
        # T: O(v), S: O(e)