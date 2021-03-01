import discord
from discord.ext import  commands
import random
import os
import json
import time

os.chdir("C:\\Users\\matth\\PycharmProjects\\Enbot2.0")


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["balance"])
    #Gets user's balance
    async def bal(self, ctx):
        open_account(ctx.author)
        user = ctx.author
        users = get_bank_data()

        wallet_amt = users[str(user.id)]["bank"]

        em = discord.Embed(title=f"{ctx.author.name}'s balance", color=0xFFB6C1)
        em.add_field(name="Wallet Balance", value=f"`£{wallet_amt}`")
        em.set_footer(text="Bot made by @Enmatt#8829.")
        await ctx.send(embed=em)

    @commands.command(aliases=["balancetop"])
    #Balance Top Command
    async  def baltop(self, ctx, x = 10):

        users = get_bank_data()
        baltop = {}
        total = []

        #Cycles through all balances
        for user in users:
            name = int(user)
            total_amount = users[user]["bank"] + users[user]["bank"]
            baltop[total_amount] = name
            total.append(total_amount)

        #Sorts balances from largest to smallest
        total = sorted(total, reverse=True)

        #Starts embed
        em = discord.Embed(title=f"Top {x} Richest People", description="Do .bal to find out how much money you have!", color=0xFFB6C1)

        #Cycles through x users and adds feild to the embed
        i = 1
        for amt in total:
            id_ = baltop[amt]
            member = self.bot.get_user(id_)
            name = member.name
            em.add_field(name= f"{i}. {name}", value= f"`£{amt/2}`", inline=False) #IDK why we /2 but it doesn't work without so yeh lol
            if i == x:
                break
            else:
                i += 1

        #Sends Embed
        em.set_footer(text="Bot made by @Enmatt#8829.")
        await ctx.send(embed = em)

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def beg(self, ctx):
        open_account(ctx.author)

        user = ctx.author
        users = get_bank_data()

        earnings = random.randrange(101)

        answer = [f"Steve gave you `£{earnings}` coins!",
                                     f"YOUR MUM gave you `£{earnings}`!",
                                     f"Dr. Phill gave you `£{earnings}`!",
                                     f"Belle Delphine gave you `£{earnings}`!",
                                     f"Charli D'amelio gave you `£{earnings}`!",
                                     f"Big Chungus gave you `£{earnings}`!",
                                     f"shitass gave you `£{earnings}`!",
                                     f"Enmatt gave you `£{earnings}!`",
                                     f"Someone gave you `£{earnings}!`"]

        await ctx.send(random.choice(answer))

        users[str(user.id)]["bank"] += earnings

        with open("bank.json", "w") as f:
            users = json.dump(users, f)

    @beg.error
    #Error handler for cooldown
    async def beg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = 'Woah, slow down! please try again in {:.2f}s'.format(error.retry_after)
            await ctx.send(msg)
        else:
            raise error

    @commands.command()
    async def slots(self, ctx):


        open_account(ctx.author)

        user = ctx.author
        users = get_bank_data()
        bal = users[str(user.id)]["bank"]
        if bal >= 100:

            emojis = [':apple:', ':banana:', ':strawberry:', ':cherries:', ':green_apple:', ':peach:', ':tangerine:']

            embed = discord.Embed(title=":money_mouth: Slot Machine :money_mouth:",description="React to the message to insert £100", color=0xFFB6C1)
            embed.set_footer(text="Bot made by @Enmatt#8829.")
            react = await ctx.channel.send(embed=embed)

            await react.add_reaction(u'✅')

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ['✅']

            await self.bot.wait_for('reaction_add', check=check)

            users[str(user.id)]["bank"] += -100

            i = 0

            while i <= 5:
                f1 = random.choice(emojis)
                f2 = random.choice(emojis)
                f3 = random.choice(emojis)

                embed = discord.Embed(title=":money_mouth: Slot Machine :money_mouth:", description=f"{f1}{f2}{f3}",color=0xFFB6C1)
                embed.set_footer(text="Bot made by @Enmatt#8829.")
                embed.add_field(name="Processing...", value="`¯\_(ツ)_/¯`", inline=False)
                await react.edit(embed=embed)
                time.sleep(0.5)
                i = i + 1

            if f1 == f2 == f3:
                embed = discord.Embed(title=":moneybag: Slot Machine :moneybag:", description=f"{f1}{f2}{f3}",color=0xFFB6C1)
                embed.add_field(name="You WIN!!", value="`£10,000`", inline=False)
                embed.set_footer(text="Bot made by @Enmatt#8829.")
                await react.edit(embed=embed)
                users[str(user.id)]["bank"] += 10000
            elif f1 == f2 or f1 == f3 or f2 == f3:
                embed = discord.Embed(title=":dollar: Slot Machine :dollar:", description=f"{f1}{f2}{f3}",color=0xFFB6C1)
                embed.add_field(name="You Win!", value="`£1,000`", inline=False)
                embed.set_footer(text="Bot made by @Enmatt#8829.")
                await react.edit(embed=embed)
                users[str(user.id)]["bank"] += 1000
            else:
                embed = discord.Embed(title=":sob: Slot Machine :sob:", description=f"{f1}{f2}{f3}",color=0xFFB6C1)
                embed.add_field(name="You Lose!", value="`:(`", inline=False)
                embed.set_footer(text="Bot made by @Enmatt#8829.")
                await react.edit(embed=embed)

            with open("bank.json", "w") as f:
                users = json.dump(users, f)

        else:
            await ctx.send("HAHA, TOO POOR LOL")

    @commands.command()
    async def bet(self, ctx, amount):

        amount = int(amount)

        open_account(ctx.author)

        user = ctx.author
        users = get_bank_data()
        bal = users[str(user.id)]["bank"]
        if bal >= amount:

            users[str(user.id)]["bank"] += -amount

            if random.randint(1,3) == 1:

                embed = discord.Embed(title=f"You bet £{amount}!", description="",color=0xFFB6C1)
                embed.add_field(name="You WIN!!", value=f"`£{amount*2}`", inline=False)
                embed.set_footer(text="Bot made by @Enmatt#8829.")
                await ctx.send(embed=embed)

                users[str(user.id)]["bank"] += amount*2

            else:
                embed = discord.Embed(title=f"You bet £{amount}!", description="",color=0xFFB6C1)
                embed.add_field(name="You Lose..", value=f"`:(`", inline=False)
                embed.set_footer(text="Bot made by @Enmatt#8829.")
                await ctx.send(embed=embed)

            with open("bank.json", "w") as f:
                users = json.dump(users, f)

        else:
            await ctx.send("HAHA, TOO POOR LOL")

    @bet.error
    #Error handler for no ammount
    async def bet_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            msg = 'Please make sure to specify an amount. For example: `.bet 500`'
            await ctx.send(msg)
        else:
            raise error

    @commands.command()
    async def pay(self, ctx, payee, amount):

        amount = int(amount)

        open_account(ctx.author)

        payee = payee.replace("<", "")
        payee = payee.replace(">", "")
        payee = payee.replace("@", "")
        payee = payee.replace("!", "")

        user = ctx.author
        users = get_bank_data()
        bal = users[str(user.id)]["bank"]

        if bal >= amount:

            users[str(user.id)]["bank"] += -amount
            users[str(payee)]["bank"] += amount

            embed = discord.Embed(title=f"You payed @{await self.bot.fetch_user(payee)}", description="", color=0xFFB6C1)
            embed.add_field(name=f"Amount:", value=f"`£{amount}`!", inline=False)
            embed.set_footer(text="Bot made by @Enmatt#8829.")
            await ctx.send(embed=embed)

            with open("bank.json", "w") as f:
                users = json.dump(users, f)

        else:
            await ctx.send("HAHA, TOO POOR LOL")




def open_account(user):
    users = get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["bank"] = 0

    with open("bank.json", "w") as f:
        users = json.dump(users, f)
    return True

def get_bank_data():
    with open("bank.json", "r") as f:
        users = json.load(f)

    return users

def setup(bot):
    bot.add_cog(Economy(bot))
