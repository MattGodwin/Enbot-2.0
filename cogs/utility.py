from discord.ext import commands
import discord


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Sombebody needs help!", description="Here is a list of all my commands!",
                              color=0xFFB6C1)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/754388247815258153.png?v=1")
        embed.add_field(name=".help", value="Shows a list of my commands.", inline=False)
        embed.add_field(name=".ping", value="Checks if i am responding.", inline=False)
        embed.add_field(name=".hello", value="Say hello to me.", inline=False)
        embed.add_field(name=".rps", value="Play rock, paper, scissors.", inline=False)
        embed.set_footer(text="Bot made by @Enmatt#8829.")
        await ctx.channel.send(embed=embed)


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title='Pong! :ping_pong: {0}ms'.format(round(self.bot.latency * 1000, )), color=0xFFB6C1)
        embed.set_footer(text="Bot made by @Enmatt#8829.")
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
    bot.add_cog(Ping(bot))
