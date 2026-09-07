class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet = defaultdict(list) # UserId: (time, tweetID)
        self.follower = defaultdict(set) # followerID: (followeeId, followeeId, followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follower[userId].add(userId)

        res = []
        minHeap = []

        for followeeId in self.follower[userId]:
            if followeeId in self.tweet:
                index = len(self.tweet[followeeId]) - 1
                time, tweetId = self.tweet[followeeId][index]
                minHeap.append((time, tweetId, followeeId, index - 1))
        
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweet[followeeId][index]
                heapq.heappush(minHeap, (time, tweetId, followeeId, index - 1))
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)
