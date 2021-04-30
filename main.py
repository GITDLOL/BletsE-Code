# This imports all the stuff needed 
# to make the bot working.


import mcstatus
import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive
import random
import json
from random import randint
from discord.ext.commands import Bot, has_permissions, CheckFailure
import asyncio

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

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = '**Cooling Down**, the bot is overheating, try again in {:.2f}s'.format(error.retry_after)
    await ctx.send(msg)

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
  Help=discord.Embed(title="The Help Page", description="The **Help Page** of the Bot **BletsE**", color=0x00ff00)
  Help.add_field(name="General Commands", value="📜 **This command gives a random Fact** ```>facts```\n 👿 **Pings you** ```>pingme```\n 🦾 **Gives the invite for the bot.** ```>botinvite```\n 📇 **Gives the source code for the bot** ```>sourcecode```\n 🔠 **Gives you a random word.** ```>randomword```\n 💌 **Gives you a random image** ```>randomimage```\n 😂 **Gives you a random meme**\n ```>memes```\n 🦜**Repeats what you say in an embed** ```>embedsay \"YOU HAVE TO PUT THE THINGS YOU SAY IN QUOTATION MARKS OR IT BREAKS\"```\n 🔔", inline=False)
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
  num = randint(0, 6)
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
  num = randint(0, 10)
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

  BotVer = "0.0.3u"

  BotVersion=discord.Embed(title=BotVer, description="The bot is currently on Version " + BotVer + " to see more versions click here: https://github.com/GITDLOL/BletsE-Code", color=0x00ff00)
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

@bot.command(name='slowmode')
@has_permissions(administrator=True)
async def setdelay(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)

    await ctx.send(f"The current slowmode for this channel is now {seconds} seconds!")

@bot.command(name='lockchannel')
@has_permissions(administrator=True)
async def lock(message):
    await message.channel.set_permissions(message.guild.default_role, send_messages=False)
    await message.send("Channel Locked 🔒")

@bot.command(name='unlockchannel')
@has_permissions(administrator=True)
async def unlock(message):
  await message.channel.set_permissions(message.guild.default_role, send_messages=True)
  await message.send("Channel Unlocked 🔓")

@bot.command(name='balance')
async def balance(ctx):
  await open_account(ctx.author)

  user = ctx.author
  users = await getBankData()

  walletAmount = users[str(user.id)]["wallet"]
  bankAmount = users[str(user.id)]["bank"]

  BalanceEmbed = discord.Embed(title = f"{ctx.author.name}'s balance",color = 0x00ff00)
  BalanceEmbed.add_field(name="Wallet Balance: ", value="B$" + str(walletAmount))
  BalanceEmbed.add_field(name="Bank Balance: ", value="B$" + str(bankAmount))

  await ctx.send(embed=BalanceEmbed)
  
@bot.command(name='beg')
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
  await open_account(ctx.author)

  user = ctx.author
  users = await getBankData()

  Earns = random.randrange(105)

  await ctx.send(f"You got B${Earns} from begging")

  users[str(user.id)]["wallet"] += Earns

  with open ("mainbank.json", "w") as f:
    json.dump(users,f)
  return True

@bot.command(name='deposit')
async def deposit(message, depositamount: int):
  await open_account(message.author)

  user = message.author
  users = await getBankData()

  walletAmount = users[str(user.id)]["wallet"]

  if depositamount <= walletAmount:
    users[str(user.id)]["wallet"] -= depositamount
    users[str(user.id)]["bank"] += depositamount
  else:
    return False

  await message.send("You deposited " + str(depositamount) + " B$ in your bank account") 

  with open ("mainbank.json", "w") as f:
    json.dump(users,f)
  return True

@bot.command(name='withdraw')
async def withdraw(message, withamount: int):
  await open_account(message.author)

  user = message.author
  users = await getBankData()
  
  bankAmount = users[str(user.id)]["bank"]

  if withamount <= bankAmount:
    users[str(user.id)]["wallet"] += withamount
    users[str(user.id)]["bank"] -= withamount
  else:
    return False

  await message.send("You withdrew " + str(withamount) + " B$ in your bank account") 

  with open ("mainbank.json", "w") as f:
    json.dump(users,f)
  return True

# Errors
@lock.error
async def whoami_error(error, ctx):
  if isinstance(error, CheckFailure):  
    await bot.send_message("You do not have permission")
@unlock.error
async def whoami_error(error, ctx):
  if isinstance(error, CheckFailure):  
    await bot.send_message("You do not have permission")
@setdelay.error
async def whoami_error(error, ctx):
  if isinstance(error, CheckFailure):  
    await bot.send_message("You do not have permission")

# Ignore
async def open_account(user):
  
  users = await getBankData()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["wallet"] = 150
    users[str(user.id)]["bank"] = 0

  with open ("mainbank.json", "w") as f:
    json.dump(users,f)
  return True

async def getBankData():
  with open("mainbank.json", "r") as f:
    users = json.load(f)

  return users 

# keep_alive() gives the bot 24/7 hosting.
# bot.run(TOKEN) runs the bot.

keep_alive()
bot.run(TOKEN)
