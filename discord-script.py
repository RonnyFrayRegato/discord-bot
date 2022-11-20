import random
import discord
import scraping_google_images
from discord import app_commands
from discord.ext import commands
import database_creation


class DiscordBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    # bot syncs slash commands on startup
    async def on_ready(self):
        await tree.sync(guild=discord.Object(server_id))  # causes slash commands to refresh on bot startup
        self.synced = True
        print("Bot is online")
        database_creation.connect_to_db()

# Global variables
bot = DiscordBot()
tree = app_commands.CommandTree(bot)
server_id = 1030163730538954853


@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel  # get system channel
    await channel.send(f"{member.mention} Welcome to the Server!")


@bot.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    await channel.send(f"Goodbye {member.mention}!")


@tree.command(name="hello", description="says a greeting")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}, This is a slash command!")


# shows latency between bot and discord server
@tree.command(name="ping", description="pings the user", guild=discord.Object(server_id))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! Latency: {round(bot.latency * 1000)}ms")


# gets a user question and replies with a random response.
@tree.command(name="eightball", description="fun game", guild=discord.Object(server_id))
async def self(interaction: discord.Interaction, question: str):
    responses = ["Wow that's a bad idea", "Come on dude, that's ridiculous", "Better not tell you now", "Yes", "No",
                 "Signs point to yes"
                 "Don't count on it on your life", "Without a doubt", "homie, you must be nuts", "It is certain",
                 "You may rely on it", "Cannot predict now",
                 "The magic conch says no", "The magic conch says yes", "Most likely", "Better not tell you now.",
                 "My reply is no", "My sources say no",
                 "Very doubtful"]
    await interaction.response.send_message(f"**Question:** {question}\n**Answers:** {random.choice(responses)}")


@tree.command(name="shutdown", description="turn the bot off", guild=discord.Object(server_id))
async def self(interaction: discord.Interaction):
    print("Bot is offline")
    await interaction.response.send_message("Bot is offline")
    await tree.client.close()


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def image(ctx):
    await scraping_google_images.main(ctx)


# runs the bot using security token
bot.run("__DISCORD_TOKEN__")
