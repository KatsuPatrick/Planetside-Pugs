from discord.ext import commands

from display import *
from teams import *


class AdminCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin Cog is online')

    """
    Admin Commands

    !clear_queue   
    !clear_match
     
    """

    @commands.command()  # !clear_queue
    @commands.guild_only()
    async def clear_queue(self, ctx):
        role = get(ctx.author.roles, name="PIL Pugs Staff")
        if role:
            clear_lobby()
            await ctx.channel.send(f'{ctx.author.mention} Lobby cleared!')
            await ctx.channel.send(embed=lobby_list())

    @commands.command()  # !clear_match
    @commands.guild_only()
    async def clear_match(self, ctx):
        role = get(ctx.author.roles, name="PIL Pugs Staff")
        if role:
            clear_roster()
            await ctx.channel.send(f'{ctx.author.mention} Match cleared!')


def setup(client):
    client.add_cog(AdminCog(client))
