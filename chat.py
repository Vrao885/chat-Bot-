import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):

  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
client.run('MTA2MTk2NTc1MTA2MzQxMjc4Ng.GnZEGD.YXjV8QkEtqJf-LXWAr6gNOQZYvS--Lfp8ZAYnw')