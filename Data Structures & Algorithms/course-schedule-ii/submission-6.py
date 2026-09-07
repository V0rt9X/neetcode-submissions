class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { crs: [] for crs in range(numCourses) }

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        cycle = set()
        visited = set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)

            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            
            visited.add(crs)
            cycle.remove(crs)
            res.append(crs)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
            
        return res
