from config import token, uid
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("Logged in as", bot.user.name)


@bot.event
async def on_message(message):
    # if user send a message

    if(message.author.id == uid):
        await message.add_reaction('⬆️')
        await message.add_reaction('🥜')
        await message.add_reaction('⬇️')

bot.run(token)
