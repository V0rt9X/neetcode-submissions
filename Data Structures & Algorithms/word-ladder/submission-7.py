class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patterns = defaultdict(list)

        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[: i] + "*" + w[i + 1: ]
                patterns[pattern].append(w)
        
        q = collections.deque([beginWord])
        visited = set()

        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                w = q.popleft()

                if w == endWord:
                    return steps

                visited.add(w)

                for i in range(len(w)):
                    pattern = w[: i] + "*" + w[i + 1: ]
                    for nei in patterns[pattern]:
                        if nei not in visited:
                            q.append(nei)
        
        return 0
                


