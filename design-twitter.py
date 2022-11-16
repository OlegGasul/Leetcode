from collections import defaultdict

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.timestamp = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.timestamp, tweetId])
        self.timestamp += 1

    def getNewsFeed(self, userId: int):
        tweets = []
        tweets += self.tweets[userId]

        for follower in self.followers[userId]:
            tweets += self.tweets[follower]

        tweets.sort(reverse = True)
        
        result = []
        count = 1
        for timestamp, tweetId in tweets[ : 10]:
            result.append(tweetId)
            count += 1
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)

twitter = Twitter()
twitter.postTweet(1, 5)
twitter.postTweet(1, 3)
twitter.postTweet(1, 101)
twitter.postTweet(1, 13)
twitter.postTweet(1, 10)
twitter.postTweet(1, 2)
twitter.postTweet(1, 94)
twitter.postTweet(1, 505)
twitter.postTweet(1, 333)
twitter.postTweet(1, 22)
twitter.postTweet(1, 11)
print(twitter.getNewsFeed(1))