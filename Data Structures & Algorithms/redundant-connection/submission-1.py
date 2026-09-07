class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(desc):
            anc = desc

            if anc != parents[anc]:
                anc = find(parents[anc])
                
            
            return parents[anc]
    

        def union(desc1, desc2):
            anc1, anc2 = find(desc1), find(desc2)

            if anc1 == anc2:
                return False
            
            if rank[anc1] > rank[anc2]:
                parents[anc2] = anc1
                rank[anc1] += rank[anc2]
            else:
                parents[anc1] = anc2
                rank[anc2] += rank[anc1]
            
            return True
        
        for ed1, ed2 in edges:
            if not union(ed1, ed2):
                return [ed1, ed2]
