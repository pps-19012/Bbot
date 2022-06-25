import praw
import random
import os

reddit = praw.Reddit(client_id=os.environ['CLIENT_ID'],
                    client_secret=os.environ['CLIENT_SECRET'],
                     username=os.environ['USERNAME'],
                     password=os.environ['PASSWORD'],
                     user_agent="Bbot")

def cryptocurrency():
  sub1 = reddit.subreddit("CryptoCurrency")
  hot1 = sub1.hot(limit = 30)
  random_post_number = random.randint(0,30)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.title + "\n" + post.url
          return value
