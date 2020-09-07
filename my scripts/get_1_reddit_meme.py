import praw
import requests
import shutil

reddit_client = praw.Reddit(client_id="DQj9_VHwJgQ-oQ",
		client_secret="34JTpT2oxsfIqB58_RZwkbIniyo",
		password="dangerous1605",
		user_agent="a bot?",
		username="mulitate4",)
print(reddit_client.user.me())

for x in range(0, 6):
	req = reddit_client.subreddit("memes").random()

	if "jpg" in req.url or "png" in req.url:
		print (req.url)
		res = requests.get(req.url, stream=True)
		filename = req.url.split("/")[-1]

		if res.status_code == 200:
			res.raw.decode_content = True
			with open(filename,'wb') as f:
				shutil.copyfileobj(res.raw, f)
			break
		else:
			print("Image couldnt be retrieved lmao")
			continue

	else:
		print("Post wasnt an image try again")
		continue
