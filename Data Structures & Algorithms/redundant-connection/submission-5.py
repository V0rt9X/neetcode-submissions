class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        par = [i for i in range(n)]
        rank = [1] * n

        def find(desc):
            anc = desc

            while anc != par[anc]:
                par[anc] = find(par[anc])
                anc = par[anc]
            
            return anc
        
        def union(ed1, ed2):
            anc1, anc2 = find(ed1), find(ed2)

            if anc1 == anc2:
                return True
            
            if rank[anc1] <= rank[anc2]:
                par[anc1] = anc2
                rank[anc2] += rank[anc1]
            else:
                par[anc2] = anc1
                rank[anc1] += rank[anc2]
            
            return False
        
        for ed1, ed2 in edges:
            if union(ed1, ed2):
                return [ed1, ed2]
        