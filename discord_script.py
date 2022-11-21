import sys
import random
import discord
import scraping_google_images
# import database_creation
from discord import app_commands
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Global variables
server_id = 1030163730538954853


@client.event
async def on_ready():
    print("Bot is online")
    # database_creation.connect_to_db()


@client.event
async def on_member_join(member):
    channel = member.guild.system_channel  # get system channel
    await channel.send(f"{member.mention} Welcome to the Server!")


@client.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    await channel.send(f"Goodbye {member.mention}!")


@client.command(name="hello")
async def hello(ctx):
    await ctx.reply(f"Hey {ctx.author.mention}!")


# shows latency between bot and discord server
@client.command(name="ping")
async def ping(ctx):
    await ctx.reply(f"Pong! Latency: {round(client.latency * 1000)}ms")


# gets a user question and replies with a random response.
@client.command(aliases=["8ball", "8b"])
async def eightball(ctx, *, question):
    responses = ["Wow that's a bad idea", "Come on dude, that's ridiculous", "Better not tell you now", "Yes", "No",
                 "Signs point to yes",
                 "Don't count on it", "Without a doubt", "You must be nuts", "It is certain",
                 "You may rely on it", "Cannot predict now",
                 "The magic conch says no", "The magic conch says yes", "Most likely", "Better not tell you now",
                 "My reply is no", "My sources say no", "Very doubtful"]
    await ctx.send(f":8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)}")


@client.command(alias="shutdown")
async def shutdown(ctx):
    await ctx.send("Bot is offline")
    await client.close()


@client.command()
async def image(ctx):
    await scraping_google_images.main(ctx)


# runs the bot using security token
client.run(sys.argv[1])
