import discord
from discord.ext import commands
import os
from os.path import join, dirname
from dotenv import load_dotenv
import asyncio
import random
import re
command_prefix = "*"
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class bigbotsalvia(discord.Client):

    async def on_ready(self):
        print("bot starting....")
  
    async def on_message(self, message):
        if(not message.author.bot):
            if ("#justice" in message.content.lower()):
                await message.channel.send(content="https://www.gofundme.com/f/6b5bjy-justiceforjosh?utm_source=customer&utm_medium=copy_link&utm_campaign=p_cf+share-flow-1")
            if (message.content.startswith(command_prefix + "test")):
                await message.channel.send(content="teesting messaging")
            if ("#swagapinos" in message.content.lower()):
                num = random.randint(1,7)
                with open("pictures/daniel/" + str(num) + ".jpg", 'rb') as f:
                    picture = discord.File(f)
                await message.channel.send(file=picture)
            if (message.content.startswith("#pig")):
                # regexp = re.compile('[<@!](.+)\>')
                # user = 
                # print(user['match']) 
                author = message.author
                pfp = author.avatar_url
                print(pfp)
                img_data = requests.get(pfp).content
                with open('userimg.jpg', 'wb') as handler:
                    handler.write(img_data)
                avatarimage = Image.open('userimg.jpg')
                pigimage = Image.open('pictures/pigs/1.jpg')
                avatarimage = avatarimage.resize((700,700))
                position = (int((pigimage.width/2 - avatarimage.width/2)), int(pigimage.height/2 - avatarimage.height/2))
                pigimage2 = pigimage.copy()
                pigimage2.paste(avatarimage, position)
                x,y = pigimage2.size
                eX, eY = 550,550
                im = Image.new
                mask = Image.new("L", pigimage2.size, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((x/2 - eX/2,y/2 - eY/2,x/2 + eX/2,  y/2 + eY/2), fill=255)
                mask_blur = mask.filter(ImageFilter.GaussianBlur(10))
                im = Image.composite(pigimage2, pigimage, mask_blur)
                im.save("pig.png")
                with open("piguser/pig.png", "rb") as f:
                        picture = discord.File(f)
                        await message.channel.send(file=picture, content=" pig")
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='Relatively simple music bot example')

client = bigbotsalvia()
client.run(os.getenv("DISCORD_TOKEN"))
#random frankie muniz picture