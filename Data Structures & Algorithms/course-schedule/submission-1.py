class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visited = set()

        for cour, pre in prerequisites:
            preMap[cour].append(pre)
        
        def dfs(cour):
            if cour in visited:
                return False
            if preMap[cour] == []:
                return True
            
            visited.add(cour)

            for pre in preMap[cour]:
                if not dfs(pre):
                    return False
            
            visited.remove(cour)
            preMap[cour] = []

            return True
        
        for cour in range(numCourses):
            if not dfs(cour):
                return False
        
        return True