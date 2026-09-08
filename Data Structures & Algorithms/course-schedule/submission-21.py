class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {src: [] for src in range(numCourses)}

        for src, dst in prerequisites:
            preMap[src].append(dst)

        visited = {}

        def dfs(src):
            if src in visited:
                return visited[src]
            
            visited[src] = True
            for nei in preMap[src]:
                if dfs(nei):
                    return True
            
            visited[src] = False
            
            return False
        
        for src in range(numCourses):
            if dfs(src):
                return False
        
        return True