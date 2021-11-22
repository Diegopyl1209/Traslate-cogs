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
class gfn(commands.Cog):
    """Jueves de Geforce now Cog"""
    def __init__(self, bot: bot.Red):
        self.bot = bot
        self.conf = Config.get_conf(self, identifier=123400007890, force_registration=True)
        self.conf.register_guild(channel=[])
        self.check_list.start()

    @tasks.loop(seconds=10)
    async def check_list(self):
        r = requests.get("https://api-geforce-now-thursday.herokuapp.com/")
        
        channel_id = 743921141864988743
        channel = self.bot.get_channel(channel_id)  

        json_data = r.json()
        embed=discord.Embed(title="Añadidos Geforce Now", description="", color=discord.Color.green())
        embed.set_thumbnail(url="https://www.apkmirror.com/wp-content/uploads/2020/09/36/5f626fb02b86b.png")
        verify = False

        for i in json_data["games"].split(";"):
            if i in gfn:
                verify = False
            else:
                embed.add_field(name="-------------------------------------", value=i, inline=False)
                gfn.append(i)
                verify = True

        if verify == True:
            await channel.send(embed = embed)
            return embed
        else:
            pass


    def cog_unload(self):
        self.check_list.cancel()

    @commands.group()
    async def Gfn(self):
        """por el momento nada"""
        pass

    @checks.admin_or_permissions(manage_guild=True)
    @commands.guild_only()
    @Gfn.command()
    async def demo(self, ctx: commands.Context):
        """tal ves envie el ultimo embed con los juegos
        """
        embed = "nada"
        if not embed:
            await ctx.send("Todavia no esta listo")
        else:
            await ctx.send("nada")



