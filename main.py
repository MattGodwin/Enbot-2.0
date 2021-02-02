import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='.', help_command=None, intents=discord.Intents.all())
client = discord.Client()
initial_extensions = ['cogs.greetings', 'cogs.utility', 'cogs.games']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print('Online')
    await bot.change_presence(activity=discord.Game(name='Pycharm'))

bot.run('NzU2MTk3NjQ3OTA3NTUzMzEw.X2OV8A.y3djfprgRq5RsNIsyqE0dqk60sQ')
