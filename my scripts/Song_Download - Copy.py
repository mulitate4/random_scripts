import sys
import webbrowser
from time import sleep
from apiclient.discovery import build

api_key = 'AIzaSyDnRq2F3eT2IHXQkZsZDzjO_1v_JvY7HsQ'
youtube = build('youtube', 'v3', developerKey=api_key)


'''ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '0'
	}],
	'postprocessor_args': [
		'-ar', '16000'
	],
	'prefer_ffmpeg': True,
	'keepvideo': False
}'''


if len(sys.argv) < 2:
	print('Enter Song/Query')
	query = input()
else:
	query = sys.argv[1:]


'''res = youtube.search().list(q=query, part='snippet', type='video', maxResults=1)

req = res.execute()

for item in req['items']:
	print(item['snippet']['title'])
	video = pafy.new('https://youtube.com/watch?v=' + item['id']['videoId'])
	bestaudio = video.getbestaudio()
	bestaudio.extension
	sleep(1)
	bestaudio.download()

sleep(2)

'''


webbrowser.get().open_new('youtube.com/watch?v=' + item['id']['videoId'])
webbrowser.get().open_new('youtubepp.com/watch?v=' + item['id']['videoId'])
pyperclip.copy('youtube.com/watch?v=' + item['id']['videoId'])
