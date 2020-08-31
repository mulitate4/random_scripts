import praw
import pandas as pd

reddit_client = praw.Reddit(client_id="DQj9_VHwJgQ-oQ",
		client_secret="34JTpT2oxsfIqB58_RZwkbIniyo",
		password="dangerous1605",
		user_agent="a bot?",
		username="mulitate4",)

url_list = []
print(reddit_client.user.me())
req = reddit_client.subreddit("dankmemer").top(limit=50)

for q in req:
	if "jpg" in q.url or "png" in q.url:
		print (q.url)
		url_list.append(q.url)

df = pd.DataFrame(url_list)
df.to_csv('redit_urls.csv', index=False)
