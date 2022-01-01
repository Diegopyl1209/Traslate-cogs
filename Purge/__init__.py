# -*- coding: utf-8 -*-
from .purge import Purge

async def setup(bot):
    bot.add_cog(Purge(bot))