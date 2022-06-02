from datetime import datetime

from conf import configs


dt = datetime.now

def is_allowed(ctx, allow_direct=False):
    if ctx.guild:
        if ctx.guild.name in configs.GUILDS:
            return True
        else:
            return False
    else:
        return allow_direct


def debug_stuff(ctx):
    print(f'{dt().strftime("%d-%m %H:%M:%S")}  {ctx.command}  {ctx.author}/{ctx.guild}')


async def send_over_2000(ctx, text):
    while len(text) > 1996:
        await ctx.send(f'{text[:1996]}```\n')
        text = f'```\n{text[1996:]}'
    await ctx.send(text)


def generate_url(url, kwargs):
    for i in kwargs:
        url += f'&{i}={kwargs[i]}'
    return url
