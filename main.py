# This imports all the stuff needed 
# to make the bot working.


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
  await bot.change_presence(activity=discord.Game(name=f"Made By THISFLIP | {len(bot.guilds)} servers"))
  print(f'{bot.user.name} IS UP')

  
# Bot's Error if you run
# a command during the Cooldown.

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = '**Cooling Down**, the bot is overheating, try again in {:.2f}s'.format(error.retry_after)
    await ctx.send(msg)

# -------- COMMANDS --------

# Some Commands Might not make it in the final release, so any command with a "%" may not make it to the final release

# >help (DMs you the help m enu)
# >botinvite (Gives you thte invite for the bot)
# >credits (Gives you the credits for the bot [incomplete])
# >facts (Gives you a random fact)
# >sourcecode (Leads you to the bot's source code)
# >memes (Gives you a random dead meme [The current memes are temporary and are only placeholders])
# >randomword (Gives you a random word)
# >randomimage (Gives you a random image)
# >randomname (Gives you a random name)
# >embedsay (Puts everything you say in an embed)
# >botversion (Gives you the bot's current version)
# >randomwebsite (Gives you a ranrdom useless website [None are NSFW])
# >slowmode [seconds] (Makes it so that you can set a slowmode for a specific channel, very useful for if you want specific slowmode numbers)
# >lockchannel (Locks the current channel)
# >unlockchannel (Unlocks the current channel)
# >ban [user] [reason] (Bans specific user and gives the specific reason)
# >kick [user] (Kicks the specific user)

# -------- ANYTHING BELOW THIS POINT ARE ECONOMY COMMANDS --------
# >balance (Get's your balance, if you don't have an account yet it will always show B$150 in your balance
# >beg (When you beg, you have a chance of getting B$105 or a flat out B$0
# >deposit [amount] (Puts the amount you specified from your wallet to your bank)
# >withdraw [amount] (Puts the amount you specified from your bank to your wallet)
# >bet [amount] (Bets the amount of money)


@bot.command(name='help')
async def help(message):
  await message.send("Check your DMs ✅")
  Help = discord.Embed(title='BletsE The Bot\'s Help Menu\n', description='The Prefix is: **>**')
  Help.add_field(name='Random Commands', value='>randomword\n>randomimage\n>randomname\n>randomwebsite\n>facts\n>memes\n>sourcecode')
  Help.add_field(name='Info Commands', value='>botinvite\n>credits\n>sourcecode\n>botversion')
  Help.add_field(name='Administrator Commands', value='>ban `user` `reason`\n>kick `user`\n>slowmode `amount`\n>lockchannel\n>unlockchannel\n>delete `msgamount`\n>nuke')
  Help.add_field(name='Economy Commands', value='>balance\n>beg\n>deposit `amount`\n>withdraw `amount`\n>daily\n>weekly\n>bet `amount`')
  Help.add_field(name='Misc Commands', value='>embedsay `\"PUT TEXT IN QUOTE MARKS\"`\n>mybotperms\n>calculator `mathquestion`\n>userinfo\n>hack `user`')

  await message.author.send(embed=Help)

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

  sourceCode = discord.Embed(title="The Source code for my bot: ", description="https://github.com/GITDLOL/BletsE-Code")
  await message.send(embed=sourceCode)

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

  await message.send("You deposited B$" + str(depositamount) + " in your bank account") 

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

  await message.send("You withdrew B$" + str(withamount) + " in your bank account") 

  with open ("mainbank.json", "w") as f:
    json.dump(users,f)
  return True

@bot.command(name='mybotperms')
async def balance(ctx):
  await get_perms(ctx.author)

  user = ctx.author
  users = await getRankData()

  CurRank = users[str(user.id)]["rank"] 

  BalanceEmbed = discord.Embed(title = "**Your rank is: **", description=CurRank, color = 0x00ff00)

  await ctx.send(embed=BalanceEmbed)

@bot.command(name='daily')
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(message):
  await open_account(message.author)

  user = message.author
  users = await getBankData()

  Earnings = 25000

  await message.send(f'As your daily reward you got B${Earnings}')

  users[str(user.id)]["wallet"] += Earnings

  with open ("mainbank.json", "w") as f:
    json.dump(users,f)
  return True

@bot.command(name='weekly')
@commands.cooldown(1, 604800, commands.BucketType.user)
async def weekly(message):
  await open_account(message.author)

  user = message.author
  users = await getBankData()

  Earnings = 200000

  await message.send(f'As your weekly reward you got B${Earnings}')

  users[str(user.id)]["wallet"] += Earnings

  with open ("mainbank.json", "w") as f:
    json.dump(users,f)
  return True

@bot.command(name='calculator')
async def calc(message, number: int, operator, secondNumber: int):

  if operator == "+":
    result = number + secondNumber
  elif operator == "-":
    result = number - secondNumber
  elif operator == "*":
    result = number * secondNumber
  elif operator == "x":
    result = number * secondNumber
  elif operator == "/":
    result = number // secondNumber
  else:
    await message.send("That is not a valid operator")

  ResultEmbed = discord.Embed(title="The result is: ", description=result, color=0x00ff00)

  await message.send(embed=ResultEmbed)

@bot.command(name='bet')
@commands.cooldown(1, 15, commands.BucketType.user)
async def bet(message, betamount: int):
  await open_account(message.author)

  user = message.author
  users = await getBankData()
  walletAmount = users[str(user.id)]["wallet"]

  RNG = random.randrange(20)

  if RNG == 10:

    if walletAmount == betamount:
      users[str(user.id)]["wallet"] += betamount
      
      BetEmbed = discord.Embed(title="You won!", color=0x00ff00)
      await message.send(embed=BetEmbed)
    else:
      await message.send("You don't have enough money.")

  else:
    if walletAmount == betamount:
      users[str(user.id)]["wallet"] -= betamount
      
      BetEmbed = discord.Embed(title="You lost!", color=0x00ff00)
      await message.send(embed=BetEmbed)
    else:
      await message.send("You do not have enough money")

  with open ("mainbank.json", "w") as f:
    json.dump(users,f)
  return True

@bot.command(name='ban')
@has_permissions(administrator=True)
async def ban(message, memberName : discord.Member, *, memberReason=None):
  await memberName.ban(reason = memberReason)
  await message.send(f'{memberName} was banned')

@bot.command(name='kick')
@has_permissions(administrator=True)
async def ban(message, memberName : discord.Member, *, memberReason=None):
  await memberName.kick(reason = memberReason)
  await message.send(f'{memberName} was kicked')

@bot.command(name='delete')
@has_permissions(administrator=True)
async def clear(ctx, amount = 1):
  await ctx.channel.purge(limit=amount)
  await ctx.channel.purge(limit=1)  

@bot.command(name='nuke')
@has_permissions(administrator=True)
async def nuke(ctx, channel: discord.TextChannel = None):
  if channel == None: 
    await ctx.send("You did not mention a channel!")
    return

  nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

  if nuke_channel is not None:
    new_channel = await nuke_channel.clone(reason="Has been Nuked!")
    await nuke_channel.delete()
    await new_channel.send("The channel has been nuked. https://tenor.com/view/nuke-bomb-deaf-dool-explode-gif-14424973")

  else:
    await ctx.send(f"No channel named {channel.name} was found!")

@bot.command(name='userinfo')
async def getInfo(message):
  userCreation = message.author.created_at.strftime("%b %d, %Y")

  userEmbed = discord.Embed(title=f'{message.author}')
  userEmbed.add_field(name='Your User ID', value=f'{message.author.id}')
  userEmbed.add_field(name='Joined Date', value=userCreation)
  await message.send(embed=userEmbed)

@bot.command(name='hack')
async def hack(message, memberHack):

  RandomPass = [
    "\"sammylol7\"",
    "\"iLoveICEcream\"",
    "\"whatMCs*it\"",
    "\"n**ga90\""
  ]

  RandomDMs = [
    "\"I love cookies\"",
    "\"show me the things\"",
    "\"what's the server ip?\""
  ]

  randDM = random.choice(RandomDMs)
  randPass = random.choice(RandomPass)

  await message.send("Hacking " + memberHack + "...")
  
  await message.send("Getting TCP Packets...")
  
  await message.send("Bruteforcing into account...")
  
  await message.send("Getting Discord Password...")
  
  await message.send("Checking DMs...")

  await message.send("Bruteforcing into network...")
  
  await message.send("Getting IP Address...")

  await message.send("Failed to get IP Address")
  
  await message.send(memberHack + "\'s last DM was " + randDM)
  
  await message.send(memberHack + "\'s password is " + randPass)

# Ignore
async def get_perms(user):
  
  users = await getRankData()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["rank"] = "💬 Bot User"

  with open ("ranks.json", "w") as f:
    json.dump(users,f)
  return True

async def getRankData():
  with open("ranks.json", "r") as f:
    users = json.load(f)

  return users


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
