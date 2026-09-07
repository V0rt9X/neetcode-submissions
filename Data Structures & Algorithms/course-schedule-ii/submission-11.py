class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {src: [] for src in range(numCourses)}

        for a, b in prerequisites:
            adj[a].append(b)
        
        visited = {}
        res = []

        def dfs(src):
            if src in visited:
                return visited[src]
            
            visited[src] = True
            for nei in adj[src]:
                if dfs(nei):
                    return True
            
            res.append(src)
            visited[src] = False
            return False
        
        for src in range(numCourses):
            if dfs(src):
                return []
        
        return res