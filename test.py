import discord
import time

client = discord.Client()


validusers = ["mustafahmetoglu#8053","chøѕeη ✘#0001"]
convertedArray = []
for user in validusers:
    newuser = user.split("#")[0]
    convertedArray.append(newuser)
print(convertedArray)
@client.event
async def on_message(message):
    x = True
        
    if str(message.author).split("#")[0] in convertedArray :
        if x == True:
            if message.content.find("!haribo") != -1:
                await message.channel.send(f"""botu çalıştıran:{message.author}""")
                while (x == True):
                    await message.channel.send("bot çalışıyo")  # If the user says !hello we will send back hi
                    time.sleep(0.2)
            elif message.content.find("!biduraq") != -1:
                while(x):
                    await message.channel.send("tamam gıral sakin")
                    time.sleep(0.2)
                    x = False

client.run("token goes here",bot=False)
