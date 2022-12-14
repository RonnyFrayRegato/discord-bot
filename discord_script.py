import sys
import random
import discord
import scraping_google_images
import database_creation
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Global variables
server_id = 1030163730538954853


@client.event
async def on_ready():
    print("Bot is online")
    database_creation.connect_to_db()
    database_creation.init_table()


# client events
@client.event
async def on_member_join(member):
    channel = member.guild.system_channel  # get system channel
    database_creation.init_user_for_msg_count(member.id)
    await channel.send(f"{member.mention} Welcome to the Server!")


@client.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    database_creation.delete_user_from_msg_count(member.id)
    await channel.send(f"Goodbye {member.mention}!")


@client.event
async def on_message(message):
    database_creation.increase_user_msg_count(message.author.id)
    await client.process_commands(message)


# moderation commands
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} has been kicked from the server.')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} has been banned from the server.')


@client.command()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def clear(ctx, amount=6):
    amount = amount + 1
    if amount > 101:
        await ctx.send("Cannot delete more than 100 messages.")
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Cleared {amount - 1} messages.")


# basic commands
@client.command(name="hello")
async def hello(ctx):
    await ctx.reply(f"Hey {ctx.author.mention}!")


@client.command(name="mycount")
async def mycount(ctx):
    count = database_creation.show_user_msg_count(ctx.author.id)
    await ctx.reply(f"Hey {ctx.author.mention} your count is {count}!")


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
    await ctx.send(f"???? Question: {question}\n???? Answer: {random.choice(responses)}")


@client.command(alias="shutdown")
async def shutdown(ctx):
    await ctx.send("Bot is offline")
    await client.close()


@client.command()
async def image(ctx):
    await scraping_google_images.main(ctx)


# runs the bot using security token
client.run(sys.argv[1])
