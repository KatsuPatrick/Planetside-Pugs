from discord.ext import commands

from factions import *
from display import *
from teams import *
from other import *


class CaptainCog(commands.Cog):
    """
    A class used to contain all of the captain commands

    Methods
    -------
    on_ready(self)
        Prints that the cog is running on startup
    """

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Captain Cog is online')

    """
    Team-Captain Commands:

    !faction
    !pick
    """

    @commands.command()  # !faction [VS/NC/TR]
    @commands.guild_only()
    async def faction(self, ctx):
        if ctx.author.id in captains:
            if len(factions_team) == 2:
                await ctx.channel.send(
                    f'{ctx.author.mention}, you have already picked a faction! Please pick a player instead.')
            elif not ctx.message.content[9:] in get_faction():
                await ctx.channel.send(
                    f'{ctx.author.mention} {ctx.message.content[9:]} is not a valid faction. Choose either ' + ", ".join(
                        get_faction()))
            else:
                set_faction_team(ctx.message.content[9:], captains.index(ctx.author.mention))
                pick_switch()
                await ctx.channel.send(f'{ctx.author.mention} picked {ctx.message.content[9:]}!')
        else:
            await ctx.channel.send(f'{ctx.author.mention} it is not your turn to pick!')

    @commands.command()  # !pick [@member]
    @commands.guild_only()
    async def pick(self, ctx, member: discord.Member):
        if ctx.author.id == team_pick_captain:
            if len(factions_team) != 2:
                await ctx.channel.send(f'{ctx.author.mention} please pick your faction first')
            elif member.mention not in roster:
                await ctx.channel.send(f'{ctx.author.mention}, you cannot pick {member.mention}')
            else:
                add_roster(member.mention, captains.index(ctx.author.mention))
                pick_switch()
                await ctx.channel.send(f'{ctx.author.mention} picked {member.mention}!')
                await ctx.channel.send(embed=match_list())
        else:
            await ctx.channel.send(f'{ctx.author.mention} it is not your turn to pick!')
        if not roster:
            clear_match()
            await ctx.channel.send('Teams and factions are picked, prepare to play!')


def setup(client):
    client.add_cog(CaptainCog(client))
