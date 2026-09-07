class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { crs: [] for crs in range(numCourses) }

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        cycle = set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            res.append(crs)
            cycle.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res