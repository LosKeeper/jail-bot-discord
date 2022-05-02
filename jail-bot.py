from config import token, uid
import discord
from discord.ext import commands
from discord.utils import get
import asyncio

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("Logged in as", bot.user.name)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="everyone sending peanuts"))


@bot.event
async def on_message(message):
    if(message.author.id == uid):
        await message.add_reaction('⬆️')
        await message.add_reaction('🥜')
        await message.add_reaction('⬇️')


@bot.event
async def on_raw_reaction_add(payload):
    if payload.emoji.name == '🥜':
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        if message.author.id == uid:
            reaction = get(message.reactions, emoji=payload.emoji.name)
            if reaction and reaction.count == 2:
                member = discord.Member
                member.id = uid
                await mute(channel, member, 10)


# mute command
async def mute(ctx, member: discord.Member, mute_time: int):
    if not member:
        await ctx.send("Who do you want me to mute?")
        return
    muted = get(ctx.guild.roles, id=970710834105950288)
    membre = get(ctx.guild.roles, id=885801392483229727)
    await member.add_roles(muted)
    await member.remove_roles(membre)
    await ctx.send("{} has been muted for {} seconds".format(member.mention, mute_time))

    await asyncio.sleep(mute_time)
    await member.remove_roles(muted)
    await member.add_roles(membre)
    await ctx.send("{} has been unmuted".format(member.mention))

bot.run(token)
