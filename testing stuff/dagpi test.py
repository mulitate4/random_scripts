from asyncdagpi import Client

API_CLIENT = Client('ld46W9wQ8YaDiXOXG20lTt6I1Ze95bTV8SXlSqgW82EzpnRQulQBzEihXlIzMq3L')

async def wanted(image_url:str):
	response = await API_CLIENT.staticimage('wanted',image_url)
	with open('wanted.png''wb') as out:
		out.write(response.read())

import asyncio
asyncio.get_event_loop().run_until_complete(wanted())