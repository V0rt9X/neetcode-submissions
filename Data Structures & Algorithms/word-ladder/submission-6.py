class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.append(beginWord)

        patterns = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[: i] + '*' + word[i + 1: ]
                patterns[pattern].append(word)
        
        steps = 0
        q = collections.deque([beginWord])
        visited = set()

        while q:
            steps += 1
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return steps

                for i in range(len(word)):
                    pattern = word[: i] + '*' + word[i + 1: ]
                    for nei in patterns[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
        
        return 0