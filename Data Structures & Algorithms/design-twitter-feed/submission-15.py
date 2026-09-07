class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetM = defaultdict(list) # userID : [(time, tweetId)]
        self.followM = defaultdict(set) # followerId : [followeeId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetM[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []

        self.followM[userId].add(userId)
        for followeeId in self.followM[userId]:
            if followeeId in self.tweetM:
                index = len(self.tweetM[followeeId]) - 1
                time, tweetId = self.tweetM[followeeId][index]
                heapq.heappush(maxHeap, (time, tweetId, followeeId, index - 1))
        
        while maxHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweetM[followeeId][index]
                heapq.heappush(maxHeap, (time, tweetId, followeeId, index - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followM[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followM[followerId]:
            self.followM[followerId].remove(followeeId)
