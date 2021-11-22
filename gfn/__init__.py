# -*- coding: utf-8 -*-
from .gfn import Gfn

async def setup(bot):
    bot.add_cog(Gfn(bot))