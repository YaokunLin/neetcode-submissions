class Twitter:

    def __init__(self):
        self.twitter = {}
        self.follow_map = {}
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.twitter:
            self.twitter[userId].append((self.time, tweetId))
        else:
            self.twitter[userId] = [(self.time, tweetId)]
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        if userId in self.twitter:
            news_feed.extend(self.twitter[userId])
        if userId in self.follow_map:
            for followeeId in self.follow_map[userId]:
                if followeeId in self.twitter:
                    news_feed.extend(self.twitter[followeeId])
        sorted_news_feed = sorted(news_feed, reverse=True)[:10]
            
        return [id for time, id in sorted_news_feed]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if not followerId in self.follow_map:
            self.follow_map[followerId] = {followeeId}
        else:
            self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map:
            self.follow_map[followerId].discard(followeeId)
        
