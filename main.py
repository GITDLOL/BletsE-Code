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
# >randomimage

@bot.command(name='help')
async def help(message):
  await message.send("Check your DMs ✅")
  Help=discord.Embed(title="Help Page", description="The **Help Page** of the Bot **BletsE**", color=0x00ff00)
  Help.add_field(name="All Commands", value="📜 **This command gives a random Fact** ```>facts```\n 👿 **Pings you** ```>pingme```\n 🦾 **Gives the invite for the bot.** ```>botinvite```\n 📇 **Gives the source code for the bot** ```>sourcecode```\n 🔠 **Gives you a random word.** ```>randomword```\n 💌 **Gives you a random image** ```>randomimage```\n 😂 **Gives you a random meme**\n ```>memes```\n 🦜**Repeats what you say in an embed** ```>embedsay \"YOU HAVE TO PUT THE THINGS YOU SAY IN QUOTATION MARKS OR IT BREAKS\"```", inline=False)
  await message.author.send(embed=Help)

@bot.command(name='nondmhelp')
async def nondmhelp(message):
  Help=discord.Embed(title="Help Page", description="The **Help Page** of the Bot **BletsE**", color=0x00ff00)
  Help.add_field(name="All Commands", value="📜 **This command gives a random Fact** ```>facts```\n 👿 **Pings you** ```>pingme```\n 🦾 **Gives the invite for the bot.** ```>botinvite```\n 📇 **Gives the source code for the bot** ```>sourcecode```\n 🔠 **Gives you a random word.** ```>randomword```\n 💌 **Gives you a random image** ```>randomimage```\n 😂 **Gives you a random meme**\n ```>memes```\n 🦜**Repeats what you say in an embed** ```>embedsay \"YOU HAVE TO PUT THE THINGS YOU SAY IN QUOTATION MARKS OR IT BREAKS\"```", inline=False)
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
  num = randint(0, 4)
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
  RandWordEmbed = discord.Embed(title=RandomWordsResponse)
  await message.send(embed=RandWordEmbed)

@bot.command(name='randomimage')
async def randomimage(message):
  num = randint(0, 5)
  try:
      await message.send(file = discord.File("RandImages/{}.jpg".format(num))) 
  except:
      await message.send(file = discord.File("RandImages/{}.png".format(num)))

@bot.command(name='randomname')
async def randomname(message):
  randNames = [
    "**Eric**",
    "**Adam**",
    "**Michael**",
    "**Curtis**",
    "**Tomato**",
  ]
  RandomNameResponse = random.choice(randNames)
  await message.send(RandomNameResponse)

@bot.command(name='embedsay')
async def embedsay(message, args):
  embedSay=discord.Embed(title="You said: ", description=args, color=0x00ff00)
  await message.send(embed=embedSay)

@bot.command(name='botversion')
async def botversion(message):
  BotVersion=discord.Embed(title="0.0.1 ", description="The bot is currently on Version 0.0.1 to see more versions click here: https://github.com/GITDLOL/BletsE-Code", color=0x00ff00)
  await message.send(embed=BotVersion)

@bot.command(name='randomwebsite')
async def randweb(message):
  RandomWebsites = [
    "https://www.agegeek.com/",
    "https://www.worldsdumbestgame.com/",
    "https://www.crazycardtrick.com/",
    "https://www.inherentlyfunny.com/",
    "https://hczhcz.github.io/Flappy-2048/"
  ]
  RandWebRandomizer = random.choice(RandomWebsites)
  RandWeb = discord.Embed(title="Here is your random website (Not NSFW): ", description=RandWebRandomizer)
  await message.send(embed=RandWeb)


# keep_alive() gives the bot 24/7 hosting.
# bot.run(TOKEN) runs the bot.

keep_alive()
bot.run(TOKEN)
