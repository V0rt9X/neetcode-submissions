class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {src: [] for src in range(numCourses)}

        for src, dst in prerequisites:
            preMap[src].append(dst)
        
        visited = set()

        def dfs(src):
            if src in visited:
                return False
            if not preMap[src]:
                return True
            
            visited.add(src)
            for dst in preMap[src]:
                if not dfs(dst):
                    return False
            
            visited.remove(src)
            preMap[src] = []
            
            return True
        
        for src in range(numCourses):
            if not dfs(src):
                return False
        
        return True
