class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for w in words:
            for c in w:
                adj[c] = []
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[: minLen] == w2[: minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
        
        visited = {}
        res = []

        def topol(src):
            if src in visited:
                return visited[src]
            
            visited[src] = True
            for nei in adj[src]:
                if topol(nei):
                    return True
            
            res.append(src)
            visited[src] = False
            return False
        
        for src in adj:
            if topol(src):
                return ""
        
        return "".join(res[::-1])

        # T: O(n * t), S: O(n * t)