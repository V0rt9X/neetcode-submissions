class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {src: [] for src in range(numCourses)}

        for a, b in prerequisites:
            adj[a].append(b)
        
        visited = set()
        cycle = set()
        res = []

        def dfs(src):
            if src in cycle:
                return False
            if src in visited:
                return True
            
            cycle.add(src)
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            
            res.append(src)
            visited.add(src)
            cycle.remove(src)
            return True
        
        for src in range(numCourses):
            if not dfs(src):
                return []
        
        return res