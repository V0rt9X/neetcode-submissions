class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet = defaultdict(list) # key: [(time, tweetId)]
        self.folower = defaultdict(set) # key: (id, id, id)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        self.folower[userId].add(userId)
        for followeeId in self.folower[userId]:
            for time, tweetId in self.tweet[followeeId]:
                maxHeap.append((-time, tweetId))
        
        heapq.heapify(maxHeap)

        while maxHeap and len(res) < 10:
            tweetId = heapq.heappop(maxHeap)[1]
            res.append(tweetId)
        
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.folower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.folower[followerId]:
            self.folower[followerId].remove(followeeId)
