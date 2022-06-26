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

def bnp():
  sub1 = reddit.subreddit("BeautifulNaturePhotos")
  top1 = sub1.top(limit = 150)
  random_post_number = random.randint(0,150)
  for i,post in enumerate(top1):
      if i==random_post_number:
          value = post.url
          return value

def memes():
  sub1 = reddit.subreddit("memes")
  hot1 = sub1.hot(limit = 150)
  random_post_number = random.randint(0,150)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.url
          return value

def dankmemes():
  sub1 = reddit.subreddit("dankmemes")
  hot1 = sub1.hot(limit = 150)
  random_post_number = random.randint(0,150)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.url
          return value

def redditannounce():
  sub1 = reddit.subreddit("announcements")
  hot1 = sub1.hot(limit = 150)
  random_post_number = random.randint(0,150)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.url
          return value

def worldnews():
  sub1 = reddit.subreddit("worldnews")
  hot1 = sub1.hot(limit = 100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.title + "\n" + post.url
          return value

def gaming():
  sub1 = reddit.subreddit("gaming")
  hot1 = sub1.hot(limit = 100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.title + "\n" + post.url
          return value

def music():
  sub1 = reddit.subreddit("Music")
  hot1 = sub1.hot(limit = 100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.title + "\n" + post.url
          return value

def movies():
  sub1 = reddit.subreddit("movies")
  hot1 = sub1.hot(limit = 100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.title + "\n" + post.url
          return value

def news():
  sub1 = reddit.subreddit("news")
  hot1 = sub1.hot(limit = 100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.title + "\n" + post.url
          return value

def gifs():
  sub1 = reddit.subreddit("gifs")
  hot1 = sub1.hot(limit = 100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.title + "\n" + post.url
          return value

def books():
  sub1 = reddit.subreddit("books")
  hot1 = sub1.hot(limit = 100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.title + "\n" + post.url
          return value

def sports():
  sub1 = reddit.subreddit("sports")
  hot1 = sub1.hot(limit = 100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.title + "\n" + post.url
          return value

def showerthoughts():
  sub1 = reddit.subreddit("Showerthoughts")
  hot1 = sub1.hot(limit = 100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.title + "\n" + post.url
          return value

def earth():
  sub1 = reddit.subreddit("EarthPorn")
  hot1 = sub1.hot(limit = 100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.title + "\n" + post.url
          return value

def jokes():
  sub1 = reddit.subreddit("Jokes")
  hot1 = sub1.hot(limit = 100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(hot1):
      if i==random_post_number:
          value = post.title + "\n" + post.url
          return value
