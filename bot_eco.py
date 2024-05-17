import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l-accesso come {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('raccolta_differenziata'):
        await message.channel.send("Ti faccio vedere un video per spiegartelo brevemente")
        video_url = 'https://youtu.be/mDpK_MNOg94'
        await message.channel.send(video_url)

    
# "scrivi il tuo token"
