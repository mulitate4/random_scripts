#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup

def download_xplosm(r1, r2):
	for x in range(r1, r2):
		print('downloading page https://xplosm.net/comic/%s' % (x))
		res = requests.get('http://xplosm.net/comic/%s' % (x))
		res.raise_for_status

		xplosmsoup = BeautifulSoup(res.content, 'html.parser')

		comic_elem = xplosmsoup.select('#comic-wrap')
		
		if comic_elem == []:
			print('comic not found')
			continue

		comicURL = comic_elem[0].get('src')
		comicIMG = requests.get('https:' + comicURL)

		print('downloading xplosm%s' % (x))
		imagefile = open('xplosm%s.png' % (x), 'wb')

		for chunk in comicIMG.iter_content(100000):
			imagefile.write(chunk)

print('enter range of comics to download')
x1 = int(input())
x2 = int(input())

download_xplosm(x1, x2)
