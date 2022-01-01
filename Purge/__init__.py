# -*- coding: utf-8 -*-
from .purge import purge

async def setup(bot):
    bot.add_cog(purge(bot))