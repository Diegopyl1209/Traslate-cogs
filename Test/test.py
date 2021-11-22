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


gfn = []
class Test(commands.Cog):
    """A YouTube subscription cog
    
    Thanks to mikeshardmind(Sinbad) for the RSS cog as reference"""
    has_warned_about_invalid_channels = False
    def __init__(self, bot: bot.Red):
        self.bot = bot
        self.check_list.start()



    @tasks.loop(seconds=10)
    async def check_list(self):
        r = requests.get("https://api-geforce-now-thursday.herokuapp.com/")
        
        channel = self.bot.get_channel(901904896507392061)


        #json_data = eval(r.text).split("\n•")
        json_data = r.json()
        await channel.send(json_data["games"])

        for i in json_data["games"]:
            await channel.send(i)




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