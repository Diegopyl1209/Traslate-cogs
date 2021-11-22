# -*- coding: utf-8 -*-
from .gfn import gfn

async def setup(bot):
    bot.add_cog(gfn(bot))