from asyncdagpi import Client

API_CLIENT = Client('')

async def wanted(image_url:str):
	response = await API_CLIENT.staticimage('wanted',image_url)
	with open('wanted.png''wb') as out:
		out.write(response.read())

import asyncio
asyncio.get_event_loop().run_until_complete(wanted())
