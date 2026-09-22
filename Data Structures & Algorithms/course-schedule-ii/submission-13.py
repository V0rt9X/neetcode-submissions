class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {src: [] for src in range(numCourses)}

        for src, pre in prerequisites:
            adj[src].append(pre)
        
        visited = {}
        res = []

        def topol(src):
            if src in visited:
                return visited[src]
            
            
            visited[src] = True
            for nei in adj[src]:
                if topol(nei):
                    return True
            
            visited[src] = False
            res.append(src)
            return False
        
        for src in range(numCourses):
            if topol(src):
                return []
        
        return res

        # T: O(v + e), S: O(v + e)
