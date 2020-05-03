import discord
import time

client = discord.Client()

@client.event
async def on_message(message):
    x = True
    if message.content.find("!spam aç") != -1:
        while (x):
            await message.channel.send("Bot çalışyo")  # If the user says !hello we will send back hi
            time.sleep(0.3)



client.run("token goes here",bot=False)
