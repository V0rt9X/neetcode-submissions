class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = { crs: [] for crs in range(numCourses) }

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited, cycle = set(), set()
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
            
            cycle.remove(crs)
            res.append(crs)
            visited.add(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res
        