# -*- coding: utf-8 -*-
from .Purge import purge

async def setup(bot):
    bot.add_cog(Purge(bot))