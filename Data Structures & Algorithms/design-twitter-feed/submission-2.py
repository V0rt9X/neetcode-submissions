class Twitter:

    def __init__(self):
        self.count = 0
        self.TweetMap = defaultdict(list) # ID -> [time, tweetId]
        self.FollowMap = defaultdict(set) # ID -> set(foloweeID)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.TweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.FollowMap[userId].add(userId)
        for folower in self.FollowMap[userId]:
            if folower in self.TweetMap:
                index = len(self.TweetMap[folower]) - 1
                count, tweetId = self.TweetMap[folower][index]
                minHeap.append([count, tweetId, folower, index - 1])
        
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, folower, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.TweetMap[folower][index]
                heapq.heappush(minHeap, [count, tweetId, folower, index - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.FollowMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.FollowMap[followerId]:
            self.FollowMap[followerId].remove(followeeId)
