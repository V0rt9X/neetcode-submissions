class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordNei = defaultdict(list)
        steps = 1

        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                patern = word[: i] + '*' + word[i + 1: ]
                wordNei[patern].append(word)

        q = collections.deque([beginWord])
        visited = set([beginWord])

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return steps
                
                for i in range(len(word)):
                    patern = word[: i] + '*' + word[i + 1: ]
                    for nei in wordNei[patern]:
                        if nei in visited:
                            continue
                        q.append(nei)
                        visited.add(word)
            
            steps += 1

        return 0