# -*- coding: utf-8 -*-
import asyncio
import datetime
import re
import time
import hashlib
import logging
import urllib, requests, json

import aiohttp
import discord
import feedparser

from typing import Optional

from discord.ext import tasks
from redbot.core import Config, bot, checks, commands
from redbot.core.utils.chat_formatting import pagify



with urllib.request.urlopen("https://gist.githubusercontent.com/Diegopyl1209/e9c1678c77427c20f3585f44f42767c3/raw/bf32706e2f7c43ca5206246fd3cb6bd2d3863960/gistfile1.txt") as url:
    data = json.loads(url.read().decode())
list1 = data

class Test(commands.Cog):
    """A YouTube subscription cog
    
    Thanks to mikeshardmind(Sinbad) for the RSS cog as reference"""
    has_warned_about_invalid_channels = False
    def __init__(self, bot: bot.Red):
        self.bot = bot
        self.check_list.start(list1)



    @tasks.loop(seconds=10)
    async def check_list(self, list1):
        with urllib.request.urlopen("https://gist.githubusercontent.com/Diegopyl1209/e9c1678c77427c20f3585f44f42767c3/raw/efbfb1f4505564c836133e4c026fb0afcfeffb6b/gistfile1.txt") as url:
            data1 = json.loads(url.read().decode())
        list2 = data1
        channel = self.bot.get_channel(901904896507392061)
        await channel.send("Test1")
        if True:
            for i in list2:
                if i in list1:
                    pass
                else:
                    await channel.send(i)
            await channel.send("test2")

    def cog_unload(self):
        self.check_list.cancel()

    @commands.group()
    async def test(self, ctx: commands.Context):
        """Post when new videos are added to a YouTube channel"""
        pass

    @checks.admin_or_permissions(manage_guild=True)
    @commands.guild_only()
    @test.command()
    async def subscribe(self, ctx: commands.Context, channelYouTube, channelDiscord: Optional[discord.TextChannel] = None, publish: Optional[bool] = False):
        """Establece un canal en donde se enviaran los nuevos juegos de geforce now
        """
        pass