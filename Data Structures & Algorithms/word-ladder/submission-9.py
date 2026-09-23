class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj = defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[: i] + "*" + w[i + 1: ]
                adj[pattern].append(w)
        
        q = collections.deque([beginWord])
        visited = set()

        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return steps

                visited.add(word)

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1: ]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            q.append(nei)
        
        return 0