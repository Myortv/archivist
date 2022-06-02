from discord.ext import commands
from discord import Thread, TextChannel
from conf.configs import bot, LOCATIONS_CATEGORY_ID


@bot.command(name='locations')
async def locations(ctx):
    out = ''
    for channel in ctx.guild.channels:
        if channel.category:
            if channel.category.id == LOCATIONS_CATEGORY_ID:
                out = f'{out}<#{channel.id}>\n'
    await ctx.send(out)


@bot.command(name='travel')
async def travel(ctx):
    data = ctx.message.content.split('\n')[1:]
    for target_channel in data:
        for channel in ctx.guild.channels:
            if not channel.name == target_channel or not channel.category:
                continue
            if not channel.category.id == LOCATIONS_CATEGORY_ID:
                continue
            await channel.set_permissions(ctx.author, read_messages=True)
            print(channel, target_channel)

        # if channel.category:
        #     if channel.category.id == LOCATIONS_CATEGORY_ID:
        #         await channel.set_permissions(ctx.message.author, read_messages=True)


@bot.command(name='leave')
async def leave(ctx):
    for channel in ctx.message.channel_mentions:
        if not channel.category:
            continue
        if not channel.category.id == LOCATIONS_CATEGORY_ID:
            continue
        await channel.set_permissions(ctx.author, read_messages=False)
