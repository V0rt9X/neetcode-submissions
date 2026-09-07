class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket = defaultdict(list)

        tickets.sort(reverse = True)

        for dep, arr in tickets:
            ticket[dep].append(arr)
        
        res = []

        def dfs(dep):
            while ticket[dep]:
                arr = ticket[dep].pop()
                dfs(arr)
            
            res.append(dep)
        
        dfs("JFK")
        return res[::-1]