from .roleplay import Roleplay

__red_end_user_data_statement__ = "This cog does not persistently store any PII data or metadata about users."


def setup(bot):
    n = Roleplay(bot)
    bot.add_cog(n)
