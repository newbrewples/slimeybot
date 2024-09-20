# Despise my creation as much as you need.
# it's still on Dev phase.
# - Brewy
# P.S. I suck at coding, OFC it looks primitive.

import discord
from discord.ext import commands
import io
import logging

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.messages= True
intents.message_content = True
allowed_mentions = discord.AllowedMentions(everyone = True)
bot = commands.Bot(command_prefix='*', intents=intents)

# This is for the Owner/Admin roles, replace them with ur own
ALLOWED_ROLE_IDS = []
@bot.event
async def on_ready():
    print('Your bot is ready and operative brewy.')
    
async def salute(ctx):
	await ctx.send('Hello Discord.')

@bot.command()
async def fire(ctx):
	await ctx.send('i can type stuff now... 🔥')
	
@bot.command()
async def typr(ctx, arg):
    await ctx.send(arg)	

@bot.command(name='alarm')
async def alarm(ctx):
    if any(role.id in ALLOWED_ROLE_IDS for role in ctx.author.roles):
        await ctx.send("@everyone \n# The ALARM HAS BEEN PUT OFF!\n\nwhy did it ping? cause the alarm could mean a bunch of things, like:\n\n1. The server was either raided, nuked, or both.\n\n2. A way to ***REVIVE CHAT!!!!***\n\nEither way, brewy is sorry for coding this in\n-# Alarm, idea took by saturn. adapted to python by brewy.")
    else:
        await ctx.send("ya can't ping, pesky raider 😜")


bot.run('BOT_ID_FAKU')
