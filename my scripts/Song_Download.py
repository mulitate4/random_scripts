import sys
import webbrowser
from time import sleep
from apiclient.discovery import build
import json

api_key = 'AIzaSyDnRq2F3eT2IHXQkZsZDzjO_1v_JvY7HsQ'
youtube = build('youtube', 'v3', developerKey=api_key)

print('Enter Song/Query')
query = input()

res = youtube.search().list(q=query, part='snippet', type='channel', maxResults=2)
req = res.execute()
print(req)
print(json.dumps(req))
