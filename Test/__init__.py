# -*- coding: utf-8 -*-
from .test import Test

async def setup(bot):
    bot.add_cog(Test(bot))