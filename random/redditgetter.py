import praw
import pandas as pd

reddit_client = praw.Reddit(client_id="",
		client_secret="",
		password="",
		user_agent="",
		username="",)

url_list = []
print(reddit_client.user.me())
req = reddit_client.subreddit("dankmemer").top(limit=50)

for q in req:
	if "jpg" in q.url or "png" in q.url:
		print (q.url)
		url_list.append(q.url)

df = pd.DataFrame(url_list)
df.to_csv('redit_urls.csv', index=False)
