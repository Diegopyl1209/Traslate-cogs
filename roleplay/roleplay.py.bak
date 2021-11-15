from random import choice

import discord
from redbot.core import Config, commands
from redbot.core.bot import Red
from redbot.core.commands import Context
from redbot.core.utils.chat_formatting import bold, quote

from .constants import *


class Roleplay(commands.Cog):
    """Do roleplay with your Discord friends or virtual strangers."""

    __author__ = "ow0x"
    __version__ = "1.0.3"

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthor: {self.__author__}\nCog Version: {self.__version__}"

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, 123456789987654321, force_registration=True)
        default_global = {"schema_version": 1}
        default_user = {
            "BAKAS_SENT": 0,
            "BAKAS_RECEIVED": 0,
            "BULLY_SENT": 0,
            "BULLY_RECEIVED": 0,
            "CUDDLES_SENT": 0,
            "CUDDLES_RECEIVED": 0,
            "CRY_COUNT": 0,
            "FEEDS_SENT": 0,
            "FEEDS_RECEIVED": 0,
            "HIGHFIVES_SENT": 0,
            "HIGHFIVES_RECEIVED": 0,
            "HUGS_SENT": 0,
            "HUGS_RECEIVED": 0,
            "KILLS_SENT": 0,
            "KILLS_RECEIVED": 0,
            "KISSES_SENT": 0,
            "KISSES_RECEIVED": 0,
            "LICKS_SENT": 0,
            "LICKS_RECEIVED": 0,
            "NOMS_SENT": 0,
            "NOMS_RECEIVED": 0,
            "PATS_SENT": 0,
            "PATS_RECEIVED": 0,
            "POKES_SENT": 0,
            "POKES_RECEIVED": 0,
            "PUNCHES_SENT": 0,
            "PUNCHES_RECEIVED": 0,
            "SLAPS_SENT": 0,
            "SLAPS_RECEIVED": 0,
            "SMUG_COUNT": 0,
            "TICKLES_SENT": 0,
            "TICKLES_RECEIVED": 0,
        }
        self.config.register_global(**default_global)
        self.config.register_member(**default_user)
        self.config.register_user(**default_user)
        # TODO: you can do better
        if self.bot.get_cog("General"):
            self.bot.remove_command("hug")

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def baka(self, ctx: Context, *, member: discord.Member):
        """llama a alguien BAKA con una reaccion en GIF!"""
        if member.id == ctx.me.id:
            return await ctx.send("**Ｎ Ｏ   Ｕ**")

        if member.id == ctx.author.id:
            return await ctx.send(f"{bold(ctx.author.name)}, you really are BAKA. Stupid!! 💩")

        await ctx.trigger_typing()
        baka_to = await self.config.member(ctx.author).BAKAS_SENT()
        baka_from = await self.config.member(member).BAKAS_RECEIVED()
        gbaka_to = await self.config.user(ctx.author).BAKAS_SENT()
        gbaka_from = await self.config.user(member).BAKAS_RECEIVED()
        await self.config.member(ctx.author).BAKAS_SENT.set(baka_to + 1)
        await self.config.member(member).BAKAS_RECEIVED.set(baka_from + 1)
        await self.config.user(ctx.author).BAKAS_SENT.set(gbaka_to + 1)
        await self.config.user(member).BAKAS_RECEIVED.set(gbaka_from + 1)
        embed = discord.Embed(colour=member.colour)
        message = f"_**{ctx.author.name}** le dijo a {member.mention} BAKA bahahahahaha!!!_"
        embed.set_image(url=choice(BAKA))
        footer = (
            f"{ctx.author.name} uso BAKA: {baka_to + 1} veces hasta ahora.\n"
            + f"{member.name} fue llamado BAKA: {baka_from + 1} veces hasta ahora."
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 60, commands.BucketType.member)
    async def bully(self, ctx: Context, *, member: discord.Member):
        """Intimidar a alguien en este servidor con un GIF divertido!"""
        if member.id == ctx.me.id:
            return await ctx.send("**Ｎ Ｏ   Ｕ**")

        if member.id == ctx.author.id:
            return await ctx.send(
                f"{ctx.author.mention} El auto-bullying no tiene sentido. Detente, busca ayuda."
            )

        await ctx.trigger_typing()
        bully_to = await self.config.member(ctx.author).BULLY_SENT()
        bully_from = await self.config.member(member).BULLY_RECEIVED()
        gbully_to = await self.config.user(ctx.author).BULLY_SENT()
        gbully_from = await self.config.user(member).BULLY_RECEIVED()
        await self.config.member(ctx.author).BULLY_SENT.set(bully_to + 1)
        await self.config.member(member).BULLY_RECEIVED.set(bully_from + 1)
        await self.config.user(ctx.author).BULLY_SENT.set(gbully_to + 1)
        await self.config.user(member).BULLY_RECEIVED.set(gbully_from + 1)
        embed = discord.Embed(colour=member.colour)
        message = f"_**{ctx.author.name}** bullies {member.mention}_ 🤡"
        embed.set_image(url=choice(BULLY))
        footer = (
            f"{ctx.author.name} intimidado: {bully_to + 1} veces hasta ahora a.\n{member.name} "
            + f"fue intimidado: {bully_from + 1} veces hasta ahora.\n"
            + f"Alguien llame a la policía para arrestar a {ctx.author.name}."
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def cry(self, ctx: Context):
        """Hazles saber a los demás que tienes ganas de llorar o que solo quieres llorar."""
        await ctx.trigger_typing()
        cry_count = await self.config.member(ctx.author).CRY_COUNT()
        gcry_count = await self.config.user(ctx.author).CRY_COUNT()
        await self.config.member(ctx.author).CRY_COUNT.set(cry_count + 1)
        await self.config.user(ctx.author).CRY_COUNT.set(gcry_count + 1)
        embed = discord.Embed(colour=ctx.author.colour)
        embed.description = f"{ctx.author.mention} {choice(CRY_STRINGS)}"
        embed.set_image(url=choice(CRY))
        footer = f"{ctx.author.name} ha llorado {cry_count + 1} veces en este servidor hasta ahora."
        embed.set_footer(text=footer)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def cuddle(self, ctx: Context, *, member: discord.Member):
        """Acurrucarse con un miembro del servidor!"""
        if member.id == ctx.author.id:
            return await ctx.send(
                f"{ctx.author.mention} De acuerdo con todas las leyes conocidas del juego de roles, "
                + "¡No hay forma de que puedas abrazarte! vete a abrazar con "
                + "alguien... O una almohada, si estás solo como yo.. 😔"
            )

        await ctx.trigger_typing()
        cuddle_to = await self.config.member(ctx.author).CUDDLES_SENT()
        cuddle_from = await self.config.member(member).CUDDLES_RECEIVED()
        gcuddle_to = await self.config.user(ctx.author).CUDDLES_SENT()
        gcuddle_from = await self.config.user(member).CUDDLES_RECEIVED()
        await self.config.member(ctx.author).CUDDLES_SENT.set(cuddle_to + 1)
        await self.config.member(member).CUDDLES_RECEIVED.set(cuddle_from + 1)
        await self.config.user(ctx.author).CUDDLES_SENT.set(gcuddle_to + 1)
        await self.config.user(member).CUDDLES_RECEIVED.set(gcuddle_from + 1)
        embed = discord.Embed(colour=member.colour)
        if member.id == ctx.me.id:
            message = f"Awww gracias por los abrazos, {bold(ctx.author.name)}! Muy amable de su parte. 😳"
        else:
            message = f"_**{ctx.author.name}** mimos_ {member.mention}"
        embed.set_image(url=str(choice(CUDDLE)))
        footer = (
            f"{ctx.author.name} envio: {cuddle_to + 1} abrazos hasta ahora.\n"
            + f"{'I' if member == ctx.me else member.name} "
            + f"recivio: {cuddle_from + 1} abrazos hasta ahora."
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def feed(self, ctx: Context, *, member: discord.Member):
        """Alimente a alguien de este servidor virtualmente!"""
        if member.id == ctx.author.id:
            return await ctx.send(f"_{ctx.author.mention} come {bold(choice(RECIPES))}!_")

        await ctx.trigger_typing()
        feed_to = await self.config.member(ctx.author).FEEDS_SENT()
        feed_from = await self.config.member(member).FEEDS_RECEIVED()
        gfeed_to = await self.config.user(ctx.author).FEEDS_SENT()
        gfeed_from = await self.config.user(member).FEEDS_RECEIVED()
        await self.config.member(ctx.author).FEEDS_SENT.set(feed_to + 1)
        await self.config.member(member).FEEDS_RECEIVED.set(feed_from + 1)
        await self.config.user(ctx.author).FEEDS_SENT.set(gfeed_to + 1)
        await self.config.user(member).FEEDS_RECEIVED.set(gfeed_from + 1)
        embed = discord.Embed(colour=member.colour)
        if member.id == ctx.me.id:
            message = f"OWO! Gracias por la deliciosa comida..., {bold(ctx.author.name)}! ❤️"
        else:
            message = f"_**{ctx.author.name}** alimenta a {member.mention} con algo de comida deliciosa!_"
        embed.set_image(url=choice(FEED))
        footer = (
            f"{ctx.author.name} a alimentado a otros: {feed_to + 1} veces hasta ahora.\n"
            + f"{'I' if member == ctx.me else member.name} "
            + f"recibió algo de comida: {feed_from + 1} veces hasta ahora."
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def highfive(self, ctx: Context, *, member: discord.Member):
        """Choca los cinco con un usuario!"""
        if member.id == ctx.author.id:
            return await ctx.send(
                f"_{ctx.author.mention} chocar los cinco en el espejo, supongo?_"
            )

        await ctx.trigger_typing()
        h5_to = await self.config.member(ctx.author).HIGHFIVES_SENT()
        h5_from = await self.config.member(member).HIGHFIVES_RECEIVED()
        gh5_to = await self.config.user(ctx.author).HIGHFIVES_SENT()
        gh5_from = await self.config.user(member).HIGHFIVES_RECEIVED()
        await self.config.member(ctx.author).HIGHFIVES_SENT.set(h5_to + 1)
        await self.config.member(member).HIGHFIVES_RECEIVED.set(h5_from + 1)
        await self.config.user(ctx.author).HIGHFIVES_SENT.set(gh5_to + 1)
        await self.config.user(member).HIGHFIVES_RECEIVED.set(gh5_from + 1)
        embed = discord.Embed(colour=member.colour)
        if member.id == ctx.me.id:
            message = f"_chocha los cinco de regreso {bold(ctx.author.name)}_ 👀"
            embed.set_image(url="https://i.imgur.com/hQPCYUJ.gif")
        else:
            message = f"_**{ctx.author.name}** choca los cinco con_ {member.mention}"
            embed.set_image(url=choice(HIGHFIVE))
        footer = (
            f"{ctx.author.name} envio: {h5_to + 1} high-fives hasta ahora.\n"
            + f"{'I' if member == ctx.me else member.name} "
            + f"recivio: {h5_from + 1} high-fives hasta ahora."
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def hug(self, ctx: Context, *, member: discord.Member):
        """Abraza a un usuario virtualmente en Discord!"""
        if member.id == ctx.author.id:
            return await ctx.send(
                f"{ctx.author.mention} UnO nO PuEdE AbRaZarCe A sI MiSmO!!!!!"
            )

        await ctx.trigger_typing()
        hug_to = await self.config.member(ctx.author).HUGS_SENT()
        hug_from = await self.config.member(member).HUGS_RECEIVED()
        ghug_to = await self.config.user(ctx.author).HUGS_SENT()
        ghug_from = await self.config.user(member).HUGS_RECEIVED()
        await self.config.member(ctx.author).HUGS_SENT.set(hug_to + 1)
        await self.config.member(member).HUGS_RECEIVED.set(hug_from + 1)
        await self.config.user(ctx.author).HUGS_SENT.set(ghug_to + 1)
        await self.config.user(member).HUGS_RECEIVED.set(ghug_from + 1)
        embed = discord.Embed(colour=member.colour)
        if member.id == ctx.me.id:
            message = f"Awwww ¡Gracias! ¡Tan amable de tu parte! _abraza a **{ctx.author.name}** devuelta_ 🤗"
        else:
            message = f"_**{ctx.author.name}** abraza a_ {member.mention} 🤗"
        embed.set_image(url=str(choice(HUG)))
        footer = (
            f"{ctx.author.name} dio: {hug_to + 1} abrazos hasta ahora.\n"
            + f"{'I' if member == ctx.me else member.name} "
            + f"recivio: {hug_from + 1} abrazos hasta ahora!"
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 60, commands.BucketType.member)
    async def kill(self, ctx: Context, *, member: discord.Member):
        """Intente prácticamente matar a un miembro del servidor con una reacción GIF!"""
        if member.id == ctx.me.id:
            return await ctx.send("**Ｎ Ｏ   Ｕ**")

        if member.id == ctx.author.id:
            return await ctx.send(f"{ctx.author.mention} Seppuku no está permitido en mi reloj.. 💀")

        await ctx.trigger_typing()
        kill_to = await self.config.member(ctx.author).KILLS_SENT()
        kill_from = await self.config.member(member).KILLS_RECEIVED()
        gkill_to = await self.config.user(ctx.author).KILLS_SENT()
        gkill_from = await self.config.user(member).KILLS_RECEIVED()
        await self.config.member(ctx.author).KILLS_SENT.set(kill_to + 1)
        await self.config.member(member).KILLS_RECEIVED.set(kill_from + 1)
        await self.config.user(ctx.author).KILLS_SENT.set(gkill_to + 1)
        await self.config.user(member).KILLS_RECEIVED.set(gkill_from + 1)
        embed = discord.Embed(colour=member.colour)
        message = f"_**{ctx.author.name}** intenta matar a {member.mention}!_ 🇫"
        embed.set_image(url=choice(KILL))
        footer = (
            f"{ctx.author.name} intentós: {kill_to + 1} de matar hasta ahora.\n"
            + f"{member.name} fue asesinado: {kill_from + 1} veces hasta ahora!"
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.is_nsfw()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def kiss(self, ctx: Context, *, member: discord.Member):
        """[NSFW] ¡Besa a un usuario! Solo permitido en el canal NSFW."""
        if member.id == ctx.author.id:
            return await ctx.send(
                f"Poggers {bold(ctx.author.name)}, te acabas de besar! LOL!!! 💋"
            )

        await ctx.trigger_typing()
        kiss_to = await self.config.member(ctx.author).KISSES_SENT()
        kiss_from = await self.config.member(member).KISSES_RECEIVED()
        gkiss_to = await self.config.user(ctx.author).KISSES_SENT()
        gkiss_from = await self.config.user(member).KISSES_RECEIVED()
        await self.config.member(ctx.author).KISSES_SENT.set(kiss_to + 1)
        await self.config.member(member).KISSES_RECEIVED.set(kiss_from + 1)
        await self.config.user(ctx.author).KISSES_SENT.set(gkiss_to + 1)
        await self.config.user(member).KISSES_RECEIVED.set(gkiss_from + 1)
        embed = discord.Embed(colour=member.colour)
        if member.id == ctx.me.id:
            message = f"Awwww tan amable de tu parte! _Besa a **{ctx.author.name}** de vuelta!_ 😘 🥰"
        else:
            message = f"_**{ctx.author.name}** Besa a_ {member.mention} 😘 🥰"
        embed.set_image(url=str(choice(KISS)))
        footer = (
            f"{ctx.author.name} envio: {kiss_to + 1} besos hasta ahora.\n"
            + f"{member.name} recivio: {kiss_from + 1} besos hasta ahora!"
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.is_nsfw()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def lick(self, ctx: Context, *, member: discord.Member):
        """[NSFW] ¡Lame a un usuario! Solo permitido en el canal NSFW."""
        if member.id == ctx.me.id:
            return await ctx.send(
                f"{ctx.author.mention} ¿Quieres lamer un bot? Muy cachonda! Toma, lame esto: 🍆"
            )

        await ctx.trigger_typing()
        lick_to = await self.config.member(ctx.author).LICKS_SENT()
        lick_from = await self.config.member(member).LICKS_RECEIVED()
        glick_to = await self.config.user(ctx.author).LICKS_SENT()
        glick_from = await self.config.user(member).LICKS_RECEIVED()
        await self.config.member(ctx.author).LICKS_SENT.set(lick_to + 1)
        await self.config.member(member).LICKS_RECEIVED.set(lick_from + 1)
        await self.config.user(ctx.author).LICKS_SENT.set(glick_to + 1)
        await self.config.user(member).LICKS_RECEIVED.set(glick_from + 1)
        embed = discord.Embed(colour=member.colour)
        message = (
            f"{ctx.author.mention} Poggers, solo te lamiste a ti mismo. 👏"
            if member.id == ctx.author.id
            else f"_**{ctx.author.name}** lame a_ {member.mention} 😳"
        )
        embed.set_image(url=choice(LICK))
        footer = (
            f"{ctx.author.name} a lamido a otros: {lick_to + 1} veces hasta ahora.\n"
            + f"{member.name} fue lamido: {lick_from + 1} veces hasta ahora!"
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def nom(self, ctx: Context, *, member: discord.Member):
        """Intenta morder a un miembro del servidor!"""
        if member.id == ctx.me.id:
            return await ctx.send(f"**OH NO!** _Huye_")

        message = (
            f"Waaaaaa! {bold(ctx.author.name)}, ¡Te mordiste! porque ?? 😭"
            if member.id == ctx.author.id
            else f"_**{ctx.author.name}** casualmente muerde a_ {member.mention} 😈"
        )
        await ctx.trigger_typing()
        nom_to = await self.config.member(ctx.author).NOMS_SENT()
        nom_from = await self.config.member(member).NOMS_RECEIVED()
        gnom_to = await self.config.user(ctx.author).NOMS_SENT()
        gnom_from = await self.config.user(member).NOMS_RECEIVED()
        await self.config.member(ctx.author).NOMS_SENT.set(nom_to + 1)
        await self.config.member(member).NOMS_RECEIVED.set(nom_from + 1)
        await self.config.user(ctx.author).NOMS_SENT.set(gnom_to + 1)
        await self.config.user(member).NOMS_RECEIVED.set(gnom_from + 1)
        embed = discord.Embed(colour=member.colour)
        embed.set_image(url=choice(BITE))
        footer = (
            f"{ctx.author.name} a mordido: {nom_to + 1} veces hasta ahora.\n"
            + f"{member.name} recivio: {nom_from + 1} mordidas hasta ahora!"
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def pat(self, ctx: Context, *, member: discord.Member):
        """Acaricia a un miembro del servidor con un GIF saludable!"""
        if member.id == ctx.author.id:
            return await ctx.send(f"{ctx.author.mention} _se dan palmaditas, supongo? **yay**_ 🎉")

        await ctx.trigger_typing()
        pat_to = await self.config.member(ctx.author).PATS_SENT()
        pat_from = await self.config.member(member).PATS_RECEIVED()
        gpat_to = await self.config.user(ctx.author).PATS_SENT()
        gpat_from = await self.config.user(member).PATS_RECEIVED()
        await self.config.member(ctx.author).PATS_SENT.set(pat_to + 1)
        await self.config.member(member).PATS_RECEIVED.set(pat_from + 1)
        await self.config.user(ctx.author).PATS_SENT.set(gpat_to + 1)
        await self.config.user(member).PATS_RECEIVED.set(gpat_from + 1)
        message = (
            f"Wowie! Gracias {bold(ctx.author.name)} por darme palmaditas. 😳 😘"
            if member.id == ctx.me.id
            else f"_**{ctx.author.name}** le da palmaditas a_ {member.mention}"
        )
        embed = discord.Embed(colour=member.colour)
        embed.set_image(url=choice(PAT))
        footer = (
            f"{ctx.author.name} dio: {pat_to + 1} palmadas hasta ahora.\n"
            + f"{'I' if member == ctx.me else member.name} "
            + f"recivio: {pat_from + 1} palmadas hasta ahora!"
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def poke(self, ctx: Context, *, member: discord.Member):
        """¡Molesta a tus amigos o extraños de Discord!"""
        if member.id == ctx.author.id:
            return await ctx.send(f"{bold(ctx.author.name)} quiere molestarse a sí mismo eh?!")

        await ctx.trigger_typing()
        poke_to = await self.config.member(ctx.author).POKES_SENT()
        poke_from = await self.config.member(member).POKES_RECEIVED()
        gpoke_to = await self.config.user(ctx.author).POKES_SENT()
        gpoke_from = await self.config.user(member).POKES_RECEIVED()
        await self.config.member(ctx.author).POKES_SENT.set(poke_to + 1)
        await self.config.member(member).POKES_RECEIVED.set(poke_from + 1)
        await self.config.user(ctx.author).POKES_SENT.set(gpoke_to + 1)
        await self.config.user(member).POKES_RECEIVED.set(gpoke_from + 1)
        embed = discord.Embed(colour=member.colour)
        embed = discord.Embed(colour=member.colour)
        if member.id == ctx.me.id:
            message = f"Awwww! . _Molesta a **{ctx.author.name}** de vuelta!_"
        else:
            message = f"_**{ctx.author.name}** casualmente molesta a_ {member.mention}"
        embed.set_image(url=choice(POKE))
        footer = (
            f"{ctx.author.name} dio: {poke_to + 1} toques hasta ahora.\n"
            + f"{'I' if member == ctx.me else member.name} "
            + f"recibio: {poke_from + 1} toques hasta ahora!"
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def punch(self, ctx: Context, *, member: discord.Member):
        """Golpea a alguien en Discord con una reacción GIF!"""
        if member.id == ctx.me.id:
            message = (
                f"{ctx.author.mention} trató de golpear a un bot pero falló miserablemente,\n"
                + "y en su lugar se golpeo a sí mismo.\n"
                + "Que decepcionante LMFAO! 😂 😂 😂"
            )
            em = discord.Embed(colour=await ctx.embed_colour())
            em.set_image(url="https://i.imgur.com/iVgOijZ.gif")
            return await ctx.send(content=message, embed=em)

        if member.id == ctx.author.id:
            return await ctx.send(
                f"Yo uh ..... **{ctx.author.name}**, la autolesion no"
                + " suena tan divertido. Detente, busca ayuda."
            )

        await ctx.trigger_typing()
        punch_to = await self.config.member(ctx.author).PUNCHES_SENT()
        punch_from = await self.config.member(member).PUNCHES_RECEIVED()
        gpunch_to = await self.config.user(ctx.author).PUNCHES_SENT()
        gpunch_from = await self.config.user(member).PUNCHES_RECEIVED()
        await self.config.member(ctx.author).PUNCHES_SENT.set(punch_to + 1)
        await self.config.member(member).PUNCHES_RECEIVED.set(punch_from + 1)
        await self.config.user(ctx.author).PUNCHES_SENT.set(gpunch_to + 1)
        await self.config.user(member).PUNCHES_RECEIVED.set(gpunch_from + 1)
        embed = discord.Embed(colour=member.colour)
        message = f"_**{ctx.author.name}** {choice(PUNCH_STRINGS)}_ {member.mention}"
        embed.set_image(url=choice(PUNCH))
        footer = (
            f"{ctx.author.name} envio: {punch_to + 1} golpes hasta ahora.\n"
            + f"{member.name} recivio: {punch_from + 1} golpes hasta ahora!"
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def slap(self, ctx: Context, *, member: discord.Member):
        """Abofetear a un miembro del servidor!"""
        if member.id == ctx.me.id:
            return await ctx.send("**Ｎ Ｏ   Ｕ**")

        if member.id == ctx.author.id:
            return await ctx.send(f"{ctx.author.mention} No te abofetes, eres precioso!")

        await ctx.trigger_typing()
        slap_to = await self.config.member(ctx.author).SLAPS_SENT()
        slap_from = await self.config.member(member).SLAPS_RECEIVED()
        gslap_to = await self.config.user(ctx.author).SLAPS_SENT()
        gslap_from = await self.config.user(member).SLAPS_RECEIVED()
        await self.config.member(ctx.author).SLAPS_SENT.set(slap_to + 1)
        await self.config.member(member).SLAPS_RECEIVED.set(slap_from + 1)
        await self.config.user(ctx.author).SLAPS_SENT.set(gslap_to + 1)
        await self.config.user(member).SLAPS_RECEIVED.set(gslap_from + 1)
        embed = discord.Embed(colour=member.colour)
        message = f"_**{ctx.author.name}** abofetea a_ {member.mention}"
        embed.set_image(url=choice(SLAP))
        footer = (
            f"{ctx.author.name} dio: {slap_to + 1} abofeteadas hasta ahora.\n"
            + f"{member.name} recibio: {slap_from + 1} abofeteadas hasta ahora!"
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def smug(self, ctx: Context):
        """Muestra a todos tu cara de presumido!"""
        message = f"_**{ctx.author.name}** se enorgullece de **@\u200balgo**_ 😏"
        await ctx.trigger_typing()
        smug_count = await self.config.member(ctx.author).SMUG_COUNT()
        gsmug_count = await self.config.user(ctx.author).SMUG_COUNT()
        await self.config.member(ctx.author).SMUG_COUNT.set(smug_count + 1)
        await self.config.user(ctx.author).SMUG_COUNT.set(gsmug_count + 1)
        embed = discord.Embed(colour=ctx.author.colour)
        embed.set_image(url=choice(SMUG))
        footer = f"{ctx.author.name} ha presumido {smug_count + 1} veces en este servidor hasta ahora."
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def tickle(self, ctx: Context, *, member: discord.Member):
        """Intenta hacerle cosquillas a un miembro del servidor!"""
        if member.id == ctx.author.id:
            return await ctx.send(
                f"{ctx.author.mention} Hacerse cosquillas uno mismo es aburrido!"
                + " Hacer cosquillas a los demás es más divertido, ¿verdad?? 😏"
            )

        await ctx.trigger_typing()
        tickle_to = await self.config.member(ctx.author).TICKLES_SENT()
        tickle_from = await self.config.member(member).TICKLES_RECEIVED()
        gtickle_to = await self.config.user(ctx.author).TICKLES_SENT()
        gtickle_from = await self.config.user(member).TICKLES_RECEIVED()
        await self.config.member(ctx.author).TICKLES_SENT.set(tickle_to + 1)
        await self.config.member(member).TICKLES_RECEIVED.set(tickle_from + 1)
        await self.config.user(ctx.author).TICKLES_SENT.set(gtickle_to + 1)
        await self.config.user(member).TICKLES_RECEIVED.set(gtickle_from + 1)
        embed = discord.Embed(colour=member.colour)
        if member.id == ctx.me.id:
            message = f"_Wow, bonitas habilidades para hacer cosquillas, {bold(ctx.author.name)}.'d._ 🤣 🤡"
            embed.set_image(url="https://i.imgur.com/6jr50Fp.gif")
        else:
            message = f"_**{ctx.author.name}** hace cosquillas a_ {member.mention}"
            embed.set_image(url=choice(TICKLE))
        footer = (
            f"{ctx.author.name} Cosquillas a otros: {tickle_to + 1} veces hasta ahora.\n"
            + f"{'I' if member == ctx.me else member.name} "
            + f"recibio: {tickle_from + 1} cosquillas hasta ahora!"
        )
        embed.set_footer(text=footer)

        await ctx.send(content=quote(message), embed=embed)
