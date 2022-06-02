from conf import configs
from conf.configs import bot
from art import text2art

from library.decor import prerun

from archive.bot import *
from travel.bot import *

@bot.event
async def on_ready ():
    print(text2art('Archivist', 'rand'))

@bot.command(name='check')
async def check(ctx):
    await ctx.send(ctx.channel.category.id)


@bot.event
async def on_thread_join(thread):
    print(1)
    await thread.join()
    print(2)

if __name__ == '__main__':
    bot.run(configs.TOKEN)
    # bot.load_extention('archive.bot.Archive')
