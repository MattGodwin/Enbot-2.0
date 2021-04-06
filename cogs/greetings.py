from discord.ext import commands
import discord


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):

        #Auto Role On Join
        await member.add_roles(discord.utils.get(member.guild.roles, name='Members'))
        print(f"{member} was given the {discord.utils.get(member.guild.roles, name='Members')} role.")

        #Welcome Message

        channel = member.guild.system_channel
        if channel is not None:
            embed = discord.Embed(title='Welcome @{0}.'.format(member), description="Hope that you have a good time!",color=0xFFB6C1)
            embed.set_footer(text="Bot made by @Enmatt#5802.")
            await channel.send(embed=embed)

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):

        #Hello Command

        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member


def setup(bot):
    bot.add_cog(Greetings(bot))