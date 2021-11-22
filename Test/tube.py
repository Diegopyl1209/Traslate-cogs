# -*- coding: utf-8 -*-
import asyncio
import datetime
import re
import time
import hashlib
import logging

import aiohttp
import discord
import feedparser



class Test(commands.Cog):
    """A YouTube subscription cog
    
    Thanks to mikeshardmind(Sinbad) for the RSS cog as reference"""
    has_warned_about_invalid_channels = False
    def __init__(self, bot: bot.Red):
        self.bot = bot


    @commands.group()
    async def test(self, ctx: commands.Context):
        """Post when new videos are added to a YouTube channel"""
        pass

    @checks.admin_or_permissions(manage_guild=True)
    @commands.guild_only()
    @tube.command()
    async def subscribe(self, ctx: commands.Context, channelDiscord: Optional[discord.TextChannel] = None, publish: Optional[bool] = False):
        """Subscribe a Discord channel to a YouTube channel
        
        If no discord channel is specified, the current channel will be subscribed
        
        Adding channels by name is not supported at this time. The YouTube channel ID for this can be found in channel links on videos.
        
        For example, to subscribe to the channel Ctrl Shift Face, you would search YouTube for the name, then on one of the videos in the results copy the channel link. It should look like this:
        https://www.youtube.com/channel/UCKpH0CKltc73e4wh0_pgL3g
        
        Now take the last part of the link as the channel ID:
        `[p]tube subscribe UCKpH0CKltc73e4wh0_pgL3g`
        
        Setting the `publish` flag will cause new videos to be published to the specified channel. Using this on non-announcement channels may result in errors.
        """
        json_list = json.load("gfnpc-es-ES.json")

        for a in json_list:
            if json_list[a]["id"] in json_list2[a]["id"]:
                await ctx.send("test")

    @checks.admin_or_permissions(manage_guild=True)
    @commands.guild_only()
    @tube.command()
    async def unsubscribe(self, ctx: commands.Context, channelYouTube, channelDiscord: Optional[discord.TextChannel] = None):
        """Unsubscribe a Discord channel from a YouTube channel
        
        If no Discord channel is specified and the asAnnouncement flag not set to True, the subscription will be removed from all channels"""
        subs = await self.conf.guild(ctx.guild).subscriptions()
        unsubbed = []
        if channelDiscord:
            newSub = {'id': channelYouTube,
                      'channel': {'id': channelDiscord.id}}
            unsubTarget, unsubType = self.sub_uid(newSub), 'uid'
        else:
            unsubTarget, unsubType = channelYouTube, 'id'
        for i, sub in enumerate(subs):
            if sub[unsubType] == unsubTarget:
                unsubbed.append(subs.pop(i))
        if not len(unsubbed):
            await ctx.send("Subscription not found")
            return
        await self.conf.guild(ctx.guild).subscriptions.set(subs)
        await ctx.send(f"Subscription(s) removed: {unsubbed}")

    
    def cog_unload(self):
        self.background_get_new_videos.cancel()

    @tasks.loop(seconds=1)
    async def background_get_new_videos(self):
        fetched = {}
        cache_size = await self.conf.cache_size()
        for guild in self.bot.guilds:
            update = await self._get_new_videos(guild, fetched)
            if not update:
                continue
            fetched.update(update)
            # Truncate video ID cache
            cache = await self.conf.guild(guild).cache()
            await self.conf.guild(guild).cache.set(cache[-cache_size:])

    @background_get_new_videos.before_loop
    async def wait_for_red(self):
        await self.bot.wait_until_red_ready()
        interval = await self.conf.interval()
        self.background_get_new_videos.change_interval(seconds=interval)
