class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, dst in sorted(tickets, reverse = True):
            adj[src].append(dst)
        
        res = []
        
        def topol(src):
            while adj[src]:
                dst = adj[src].pop()
                topol(dst)
            
            res.append(src)
        
        topol("JFK")
        return res[::-1]

        # O(v * Cpop + e * Cpush) -> T: O(v + e), S: O(v + e)