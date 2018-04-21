import discord
import re

DISCORD_BOT_TOKEN = 'NDM2OTcyMjYxODgzNTEwODA0.DbvRwQ.7IAKvl4-Ts8mgjEw6kQPMUiVaqM'


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if (re.search('Штил', message.content) or re.search('штил', message.content)):
        await client.send_message(message.channel, 'Эй, ты чо! Не упоминай меня!')
    # if message.content.find('парарам'):
    #     await client.send_message(message.channel, 'Эй, ты чо! Не упоминай меня!')
    # if message.content.startswith('!best'):
    #     await client.send_message(message.channel, 'Штиль самый классный!')
    # if message.content.startswith('!friend'):
    #     await client.send_message(message.channel, 'Мой лучший друг - Наумов!')
    # if message.content.startswith('!help'):
    #     await client.send_message(message.channel, 'best - Штиль расскажет кто самый лучший \n friend - Штиль расскажет кто его лучший друг')

client.run(DISCORD_BOT_TOKEN)
