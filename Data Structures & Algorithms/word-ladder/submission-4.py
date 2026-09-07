class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        patterns = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                patterns[pattern].append(word)
        
        q = collections.deque([beginWord])
        visited = set([beginWord])

        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return steps
                
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for nxt in patterns[pattern]:
                        if nxt not in visited:
                            q.append(nxt)
                            visited.add(nxt)
        
        return 0

