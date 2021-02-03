import discord
from discord.ext import  commands
import random
import os
import json

os.chdir("C:\\Users\\matth\\PycharmProjects\\Enbot2.0")


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["balance"])
    async def bal(self, ctx):
        open_account(ctx.author)
        user = ctx.author
        users = get_bank_data()

        wallet_amt = users[str(user.id)]["bank"]

        em = discord.Embed(title=f"{ctx.author.name}'s balance", color=0xFFB6C1)
        em.add_field(name="Wallet Balance", value=wallet_amt)
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
            em.add_field(name= f"{i}. {name}", value= f"{amt}", inline=False)
            if i == x:
                break
            else:
                i += 1

        #Sends Embed
        await ctx.send(embed = em)

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def beg(self, ctx):
        open_account(ctx.author)

        user = ctx.author
        users = get_bank_data()

        earnings = random.randrange(101)

        answer = [f"Steve gave you {earnings} coins!",
                                     f"YOUR MUM gave you {earnings} coins!",
                                     f"Dr. Phill gave you {earnings} coins!",
                                     f"Belle Delphine gave you {earnings} coins!",
                                     f"Charli D'amelio gave you {earnings} coins!",
                                     f"Big Chungus gave you {earnings} coins!",
                                     f"shitass gave you {earnings} coins!",
                                     f"Enmatt gave you {earnings} coins!",
                                     f"Someone gave you {earnings} coins!"]

        await ctx.send(random.choice(answer))

        users[str(user.id)]["bank"] += earnings

        with open("bank.json", "w") as f:
            users = json.dump(users, f)

    @beg.error
    async def beg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = 'Woah, slow down! please try again in {:.2f}s'.format(error.retry_after)
            await ctx.send(msg)
        else:
            raise error

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
