import discord
from discord.ext import commands
import database_creation

# discord 2.0 requires intents

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# bot start up event
@bot.event
async def on_ready():
    print("Bot is online")
    database_creation.connect_to_db()
# example of bot command (if you write !ping in chat it will return Pong)
@bot.command()
async def ping(ctx): # ctx is content or context
    await ctx.send("Pong")

@bot.event
async def on_message(message):
    print(message.author.id)
    if message.author.id == 771531394634743809:
        await message.reply("shut up ronny")
        #await message.channel.send("ronny")
# runs the bot using security token
bot.run("__DISCORD_TOKEN__")    # replace with Discord token
