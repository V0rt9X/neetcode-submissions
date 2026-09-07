class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        patternM = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[: i] + '*' + word[i + 1: ]
                patternM[pattern].append(word)
        
        visited = set([beginWord])
        q = collections.deque([beginWord])
        steps = 0

        while q:
            steps += 1
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return steps
                
                for i in range(len(word)):
                    pattern = word[: i] + '*' + word[i + 1: ]
                    for nei in patternM[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
        
        return 0


        