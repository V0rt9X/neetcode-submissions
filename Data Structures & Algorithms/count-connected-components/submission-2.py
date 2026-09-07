class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge = [i for i in range(n)]
        rank = [1] * n

        def find(desc):
            curr = desc

            while curr != edge[curr]:
                edge[curr] = edge[edge[curr]]
                curr = edge[curr]
            
            return curr
        
        def union(desc1, desc2):
            anc1, anc2 = find(desc1), find(desc2)

            if anc1 == anc2:
                return 0
            
            if anc2 > anc1:
                edge[anc1] = anc2
                rank[anc2] += rank[anc1]
            else:
                edge[anc2] = anc1
                rank[anc1] += rank[anc2]
            
            return 1



        res = n
        for ed1, ed2 in edges:
            res -= union(ed1, ed2)
        
        return res

        
