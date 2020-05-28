import discord
from random import randint

TOKEN = 'REDACTED'

client = discord.Client()

@client.event
async def on_message(message):
    if message.channel != client.get_channel('513471544433836039'):
        return

    if message.content.startswith('!midnight'):
        msg = "```Stock Market change: " + str(randint(-1,2)) + "%\n\nBank prices:\n" + \
              "Wheat : " + str(randint(1,4)) + "\n" + \
              "Timber: " + str(randint(1,4)) + "\n" + \
              "Iron  : " + str(randint(1,4)) + "\n" + \
              "Fish  : " + str(randint(1,4)) + "\n" + \
              "Stocks: " + str(randint(1,4)) + "```"
        await client.send_message(client.get_channel('470396642202484736'), msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

print("Booting...")
client.run(TOKEN)