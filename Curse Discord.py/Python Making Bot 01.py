from discord.ext import commands
from random import choice

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('\033[1;32mO bot está online!')
    print(client.user.name)
    print(client.user.id)

@client.command()
async def ping(ctx):
    await ctx.send(f'Minha latência está em:{round(client.latency * 1000)} ms')

@client.command(aliases=['8ball', 'test'])
async def ball(ctx, *, question):
    responses = ['Deus te odeia.']
    await ctx.send(f'Pergunta {question}\nResposta: {choice(responses)}')

client.run('ODk2MzYzODY0Nzg5MjUwMDQ5.YWGB5w.2el3YKAjVxcGeYFn3KUaZ8kMad8')