import discord
import json

try:
    with open('config.json', 'r') as f:
        config = json.load(f)

    token = config['bottoken']
except FileNotFoundError:
    token = os.environ['bottoken']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'hi there':
            await message.channel.send('hi there!')

client = MyClient()
client.run(token)