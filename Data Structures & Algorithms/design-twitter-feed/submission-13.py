class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetM = defaultdict(list) # (time, tweetId)
        self.followeeM = defaultdict(set) # (userID)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetM[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        self.followeeM[userId].add(userId)

        for followeeId in self.followeeM[userId]:
            if followeeId in self.tweetM:
                index = len(self.tweetM[followeeId]) - 1
                time, tweetId = self.tweetM[followeeId][index]
                maxHeap.append((time, tweetId, followeeId, index - 1))
        
        heapq.heapify(maxHeap)
        res = []
        while maxHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweetM[followeeId][index]
                heapq.heappush(maxHeap, (time, tweetId, followeeId, index - 1))
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeeM[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followeeM[followerId]:
            self.followeeM[followerId].remove(followeeId)
