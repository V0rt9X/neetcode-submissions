class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {src: [] for src in range(numCourses)}
        visited = {}
        res = []

        for src, pre in prerequisites:
            preMap[src].append(pre)

        def dfs(src):
            if src in visited:
                return visited[src]
            
            visited[src] = True
            for nei in preMap[src]:
                if dfs(nei):
                    return True
            
            visited[src] = False
            res.append(src)

            return False
        
        for src in range(numCourses):
            if dfs(src):
                return []
        
        return res