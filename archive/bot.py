
from discord.ext import commands
from discord import Thread, TextChannel
from conf.configs import bot


@bot.command(name='!')
async def to_local_archive(ctx):
    if isinstance(ctx.channel, Thread):
        await ctx.channel.parent.send(f'{ctx.message.content}\n\n@here')

@bot.command(name='!!')
async def to_global_archive(ctx):
    archive_ch = bot.get_channel(980540739048067072)
    if isinstance(ctx.channel, Thread):
        message = await ctx.channel.parent.send(f'{ctx.message.content}\n\n@here')
        await message.pin()
    await archive_ch.send(f'{ctx.message.content}\n\n@everyone')
