# -*- coding: utf-8 -*-
from .test import test

async def setup(bot):
    bot.add_cog(test(bot))