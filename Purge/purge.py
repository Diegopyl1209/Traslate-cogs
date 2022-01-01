import discord

import typing
from datetime import 
from discord.ext import tasks
from redbot.core import Config, bot, checks, commands
from redbot.core.utils.chat_formatting import pagify
from discord import User, errors, TextChannel, Forbidden


class Purge(commands.Cog):
    """Comando Purge"""
    def __init__(self, bot: bot.Red):
        self.bot = bot
        self.conf = Config.get_conf(self, identifier=1234000072890, force_registration=True)
        self.conf.register_guild(channel=[])
        
    @commands.command()
    @commands.guild_only()
    @commands.admin_or_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def purge(
        self, ctx,
        num_messages: int,
    ):
        """Clear <n> messages from current channel"""
        channel = ctx.message.channel
        await ctx.message.delete()
        await channel.purge(limit=num_messages)
        return True

    @commands.command()
    @commands.guild_only()
    @commands.admin_or_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def purge_until(
        self, ctx,
        message_id: int,
    ):
        """Clear messages in a channel until the given message_id. Given ID is not deleted"""
        channel = ctx.message.channel
        try:
            message = await channel.fetch_message(message_id)
        except errors.NotFound:
            await ctx.send("Message could not be found in this channel")
            return

        await ctx.message.delete()
        await channel.purge(after=message)
        return True
    
    @commands.command()
    @commands.guild_only()
    @commands.admin_or_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def purge_user(
        self, ctx,
        user: User,
        num_minutes: typing.Optional[int] = 5,
    ):
        """Clear all messages of <User> in every channel within the last [n=5] minutes"""
        after = ctx.message.created_at - timedelta(minutes=num_minutes)

        def check(msg):
            return msg.author.id == user.id

        await ctx.message.delete()
        for channel in await ctx.guild.fetch_channels():
            if type(channel) is TextChannel:
                try:
                    await channel.purge(limit=10*num_minutes, check=check, after=after)
                except Forbidden:
                    continue