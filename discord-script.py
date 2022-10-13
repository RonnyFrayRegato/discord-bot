import discord
from discord.ext import commands

# discord 2.0 requires intents

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# bot start up event
@bot.event
async def on_ready():
    print("Bot is online")

# example of bot command (if you write !ping in chat it will return Pong)
@bot.command()
async def ping(ctx): # ctx is content or context
    await ctx.send("Pong")

# runs the bot using security token
bot.run("MTAyOTk2NDAyODYwMjI0MTA3NQ.G4N6qN.GT-TyLbVs-J3M1TCSH-YT8uqmOnTUohgtdANII")
