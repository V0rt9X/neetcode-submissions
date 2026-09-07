class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjacency = defaultdict(list)
        tickets.sort(reverse = True)

        for src, dst in tickets:
            adjacency[src].append(dst)
        
        res = []
        def dfs(src):
            while adjacency[src]:
                dst = adjacency[src].pop()
                dfs(dst)
            
            res.append(src)
        
        dfs("JFK")
        
        return res[::-1]