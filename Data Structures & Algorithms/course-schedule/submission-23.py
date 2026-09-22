class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {src: [] for src in range(numCourses)}

        for src, pre in prerequisites:
            adj[src].append(pre)
        
        visited = set()

        def func(src):
            if src in visited:
                return False
            if adj[src] == []:
                return True
            
            visited.add(src)
            for nei in adj[src]:
                if not func(nei):
                    return False
            
            adj[src] = []
            visited.remove(src)
            return True
        
        for src in range(numCourses):
            if not func(src):
                return False
        
        return True

        # T: O(v + e), S: O(v + e)