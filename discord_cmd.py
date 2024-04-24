import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)


@bot.command()
async def broadcast(ctx, channel: discord.TextChannel, interval: int, *, message):
    async def send_message():
        await channel.send(message)

    broadcast_task = tasks.loop(seconds=interval)(send_message)
    broadcast_task.start()


@bot.command()
async def text_channel(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if existing_channel:
        await ctx.send(f'Channel "{channel_name}" already exists.')
    else:
        await guild.create_text_channel(channel_name)
        await ctx.send(f'Channel "{channel_name}" created successfully.')


@bot.command()
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f'{member.name} has been kicked.')


@bot.command()
async def ban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send(f'{member.name} has been banned.')

bot.run('YOUR_BOT_TOKEN')
