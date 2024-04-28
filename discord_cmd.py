import os
import dotenv
import discord
from discord.ext import commands, tasks
# TODO: refactor hardcode part
# TODO: modify if function is not available with DMS
# TODO: implement it in Docker
# TODO: refactor code to be more readable

dotenv.load_dotenv("./env/local.env")

intents = discord.Intents.default()
intents.members = True
bot_token = os.getenv("DISCORD_BOT_TOKEN")
server_id = os.getenv("SERVER_ID")
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def echo(ctx, *, message):
    print("Echo command received")
    await ctx.send(message)


@bot.command()
async def broadcast(ctx, channel_id: int, interval: int, *, message):
    channel = bot.get_channel(channel_id)
    if not channel:
        await ctx.send(f'Channel with ID "{channel_id}" not found.')
        return

    async def send_message():
        await channel.send(message)

    broadcast_task = tasks.loop(seconds=interval)(send_message)
    broadcast_task.start()


@bot.command()
async def text_channel(ctx, channel_name):
    # server_id = os.getenv("SERVER_ID")
    guild = bot.get_guild(1232939845450600489)
    if guild is None:
        await ctx.send('Server not found.')
        return
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if existing_channel:
        await ctx.send(f'Channel "{channel_name}" already exists.')
    else:
        await guild.create_text_channel(channel_name)
        await ctx.send(f'Channel "{channel_name}" created successfully.')


@bot.command()
async def ban(ctx, member_id: int):
    guild = bot.get_guild(1232939845450600489)
    if guild is None:
        await ctx.send("Server not found.")
        return
    member = guild.get_member(member_id)
    if member is None:
        await ctx.send("Member not found.")
        return
    await member.ban()
    await ctx.send(f"Member {member_id} has been banned.")


@bot.command()
async def kick(ctx, member_id: int):
    guild = bot.get_guild(1232939845450600489)
    if guild is None:
        await ctx.send('Server not found.')
        return
    member = guild.get_member(member_id)
    if member is None:
        await ctx.send('Member not found.')
        return
    await member.kick()
    await ctx.send(f'Member {member_id} has been kicked.')


if __name__ == "__main__":
    print("TOKEN:", f'Bot token: {bot_token}')
    bot.run(bot_token)
