class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetM = defaultdict(list) # [count, tweetId]
        self.followedM = defaultdict(set) # (id, id ,id)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetM[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = [] # [count, tweetId, folower, index]

        self.followedM[userId].add(userId)
        for follower in self.followedM[userId]:
            if follower in self.tweetM:
                index = len(self.tweetM[follower]) - 1
                count, tweetId = self.tweetM[follower][index]
                maxHeap.append([count, tweetId, follower, index - 1])
        
        heapq.heapify(maxHeap)
        while maxHeap and len(res) < 10:
            count, tweetId, follower, index = heapq.heappop(maxHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetM[follower][index]
                heapq.heappush(maxHeap, [count, tweetId, follower, index - 1])
        
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followedM[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followedM[followerId]:
            self.followedM[followerId].remove(followeeId)
