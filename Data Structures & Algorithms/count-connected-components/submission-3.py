class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(desc):
            anc = desc

            while anc != par[anc]:
                par[anc] = par[par[anc]]
                anc = par[anc]
            
            return anc
        
        def union(desc1, desc2):
            anc1, anc2 = find(desc1), find(desc2)

            if anc1 == anc2:
                return 0
            
            if rank[anc2] > rank[anc1]:
                par[anc1] = anc2
                rank[anc2] += rank[anc1]
            else:
                par[anc2] = anc1
                rank[anc1] += rank[anc2]
            
            return 1


        res = n
        for ed1, ed2 in edges:
            res -= union(ed1, ed2)
        
        return res