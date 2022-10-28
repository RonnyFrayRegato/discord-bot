import discord
from discord.ext import commands
import database_creation

# discord 2.0 requires intents

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# bot start up event
@bot.event
async def on_ready():
    print("Bot is online")
    database_creation.setup_database()
# example of bot command (if you write !ping in chat it will return Pong)
@bot.command()
async def ping(ctx): # ctx is content or context
    await ctx.send("Pong")

# runs the bot using security token
bot.run("MTAyOTk2NDAyODYwMjI0MTA3NQ.GYV45j.WewDCNINvI_Npyc-OzkI_MhCd5eqIC4VEfsCmw")    # replace with Discord token
