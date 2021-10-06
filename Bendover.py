from discord.ext import commands

# Constants used for Discord and Google API interaction
url_prefix = 'http://www.youtube.com/watch?v='

# Class for the Bendover bot
class Bendover(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
