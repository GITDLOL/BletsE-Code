# This imports all the stuff needed 
# to make the bot working.


import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive
import random
import youtube_dl
import ffmpeg
from random import randint

# This Part basically gets the bot's token 
# from a .env file

load_dotenv()
TOKEN = os.getenv('BOTTOKEN')


# Bot Prefix

bot = commands.Bot(command_prefix='>', help_command=None)

# THIS GIVES THE BOT A 
# CUSTOM PRESENCE

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name="Made By THISFLIP"))
  print(f'{bot.user.name} IS UP')

# ALL OF THE COMMANDS, HERE IS A MENU:
# 
# >help
# >pingme
# >botinvite
# >credits
# >facts
# >sourcecode
# >memes
# >randomword

@bot.command(name='help')
async def help(message):
    Help = discord.Embed(title="Help Page", description="The Official Help Page for my bot **BletsE**", color=0x00ff00)
    Help.add_field(name="Important Stuff", value="**>help**\n Brings up the Help Menu.\n\n **>botinvite**\n Tells you the bot invite link. \n\n **>credits**\n Gives all credits \n\n **>sourcecode** \n Gives you the source code to the bot.", inline=False)
    Help.add_field(name="Main Commands", value="**>pingme** \n Just Pings you. \n\n **>facts** \n Gives you a random fact. \n\n **>memes** \n Gives you a random meme. \n\n **>randomword** \n Gives you a random complicated word." )
    await message.send(embed=Help)

@bot.command(name='pingme')
async def pingme(message):
    await message.send((message.author.mention))

@bot.command(name='botinvite')
async def invitebot(message):
    await message.send("**Invite me at:** <https://bit.ly/3vIjXQ5>")

@bot.command(name='credits')
async def credits(message):
    Credits = discord.Embed(title="Credits", description="ALL THE CREDITS", color=0x00ff00)
    Credits.add_field(name="Programmers", value="THISFLIP", inline=False)
    await message.channel.send(embed=Credits)

@bot.command(name='facts')
async def wordmix(message):
  Tips = [
    "Dont kill yourself, your life still has a purpose.",
    "Dont you have homework?",
    "Did You know: You can actually use >botinvite to invite this specific bot, go ahead try it",
    "This bot was actually made by one singular person.",
    "This bot took hours to code. Not to mention a bunch of Python tutorials.",
    "This bot was coded in Python",
    "THISFLIP got banned from Secret Hideout 2.0.",
    "This bot is still a work in progress.",
    "You can use >memes to get a random meme.",
  ]
  response = random.choice(Tips)
  await message.send(response)

@bot.command(name='sourcecode')
async def sourcecode(message):
  await message.send("Here is the bot's source code: https://github.com/GITDLOL/BletsE-Code")

@bot.command(name='memes')
async def meme(message):
  num = randint(0, 5)
  try:
      await message.send(file = discord.File("MEMES/{}.jpg".format(num))) 
  except:
      await message.send(file = discord.File("MEMES/{}.png".format(num)))
@bot.command(name='randomword')
async def randomword(message):
  RandomWords = [
    "extrapolate",
    "concede",
    "sustainabality",
    "meager",
    "miniscule",
    "paltry",
  ]

  RandomWordsResponse = random.choice(RandomWords)
  await message.send(RandomWordsResponse)


# keep_alive() gives the bot 24/7 hosting.
# bot.run(TOKEN) runs the bot.

keep_alive()
bot.run(TOKEN)
