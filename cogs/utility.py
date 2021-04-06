from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, arg=None):

        if arg == None:
            embed = discord.Embed(title="Sombebody needs help!", description="Here is a list of all my commands!",color=0xFFB6C1)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/754388247815258153.png?v=1")
            embed.add_field(name=".help", value="Shows a list of commands.", inline=False)
            embed.add_field(name=".help utility", value="Shows a list of Utility commands ", inline=False)
            embed.add_field(name=".help fun", value="Shows a list of fun commands", inline=False)
            embed.add_field(name=".help eco", value="shows a list of economy commands.", inline=False)
            embed.set_footer(text="Bot made by @Enmatt#8829.")
            await ctx.channel.send(embed=embed)
        elif arg == "utility":
            embed = discord.Embed(title="Sombebody needs help with utility commands!", description="Here is a list of all my utility commands!",color=0xFFB6C1)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/754388247815258153.png?v=1")
            embed.add_field(name=".help", value="Shows a list of my commands.", inline=False)
            embed.add_field(name=".ping", value="Checks if I am responding", inline=False)
            embed.add_field(name=".suggest <suggestion>", value="Sends a suggestion to the suggestions channel.", inline=False)
            embed.set_footer(text="Bot made by @Enmatt#8829.")
            await ctx.channel.send(embed=embed)
        elif arg == "fun":
            embed = discord.Embed(title="Sombebody needs help with fun commands!", description="Here is a list of all my fun commands!",color=0xFFB6C1)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/754388247815258153.png?v=1")
            embed.add_field(name=".rps", value="Play Rock Paper Scissors.", inline=False)
            embed.add_field(name=".hello", value="Say hello!", inline=False)
            embed.set_footer(text="Bot made by @Enmatt#8829.")
            await ctx.channel.send(embed=embed)
        elif arg == "eco":
            embed = discord.Embed(title="Sombebody needs help with economy commands!", description="Here is a list of all my economy commands!",color=0xFFB6C1)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/754388247815258153.png?v=1")
            embed.add_field(name=".bal", value="Checks your balance.", inline=False)
            embed.add_field(name=".baltop", value="Shows the balance leaderboard.", inline=False)
            embed.add_field(name=".beg", value="Beg for money.", inline=False)
            embed.add_field(name=".slots", value="Play the slot machine.", inline=False)
            embed.add_field(name=".bet <amount>", value="Chance of doubling your money.", inline=False)
            embed.add_field(name=".pay <user> <amount>", value="Pay a user some money.", inline=False)
            embed.set_footer(text="Bot made by @Enmatt#8829.")
            await ctx.channel.send(embed=embed)




class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title='Pong! :ping_pong: {0}ms'.format(round(self.bot.latency * 1000, )), color=0xFFB6C1)
        embed.set_footer(text="Bot made by @Enmatt#5802.")
        await ctx.channel.send(embed=embed)


class Suggestions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suggest(self, ctx, *, suggestion):

        await ctx.send("Suggestion Sent!")

        channel = self.bot.get_channel(817438536735260682)
        user = ctx.author

        embed = discord.Embed(title=f'Suggestion', color =0xFFB6C1)
        embed.add_field(name=f'{user}', value=f'{suggestion}', inline=False)
        embed.set_footer(text="Bot made by @Enmatt#5802.")
        react = await channel.send(embed=embed)

        await react.add_reaction(u'⬆')
        await react.add_reaction(u'⬇')


def setup(bot):
    bot.add_cog(Help(bot))
    bot.add_cog(Ping(bot))
    bot.add_cog(Suggestions(bot))
