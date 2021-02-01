from discord.ext import commands
import discord
import random


class RPS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx):
        rock = u'🪨'
        paper = u'🧻'
        scissors = u'✂'
        rps = ['🪨', '🧻', '✂']

        embed = discord.Embed(title="Rock, Paper or Scissors?",
                              description="React with your choice. :rock: :roll_of_paper: :scissors:", color=0xFFB6C1)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/754388247815258153.png?v=1")
        embed.set_footer(text="Bot made by @Enmatt#8829.")
        lol = await ctx.channel.send(embed=embed)

        for em in rps:
            await lol.add_reaction(em)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['🪨', '🧻', '✂']

        reaction, user = await self.bot.wait_for('reaction_add', check=check)
        reaction = reaction.emoji
        compReaction = random.choice(rps)

        if reaction == compReaction:
            embed = discord.Embed(title="You Drew! :laughing:", description="We both chose " + reaction + "!",
                                  color=0xFFB6C1)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/662101731009757222.png?v=1")
            embed.set_footer(text="Bot made by @Enmatt#8829.")
            await lol.edit(embed=embed)

        elif reaction == rock and compReaction == paper:
            embed = discord.Embed(title="You lost! :cry:", description="I chose  🧻!", color=0xFFB6C1)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/662101731009757222.png?v=1")
            embed.set_footer(text="Bot made by @Enmatt#8829.")
            await lol.edit(embed=embed)

        elif reaction == scissors and compReaction == rock:
            embed = discord.Embed(title="You lost! :cry:", description="I chose  🪨!", color=0xFFB6C1)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/662101731009757222.png?v=1")
            embed.set_footer(text="Bot made by @Enmatt#8829.")
            await lol.edit(embed=embed)

        elif reaction == paper and compReaction == scissors:
            embed = discord.Embed(title="You lost! :cry:", description="I chose  ✂!", color=0xFFB6C1)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/662101731009757222.png?v=1")
            embed.set_footer(text="Bot made by @Enmatt#8829.")
            await lol.edit(embed=embed)

        else:
            embed = discord.Embed(title="You Won! :smile:", description="I chose" + compReaction + "!", color=0xFFB6C1)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/662101731009757222.png?v=1")
            embed.set_footer(text="Bot made by @Enmatt#8829.")
            await lol.edit(embed=embed)


def setup(bot):
    bot.add_cog(RPS(bot))