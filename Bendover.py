from discord.ext import commands
import keys.api_keys as keys
from song_queue import SongQueue
from googleapiclient.discovery import build

# Youtube Download options
ytdl_format_options = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': 'mp3',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

# Constants used for Discord and Google API interaction
url_prefix = 'http://www.youtube.com/watch?v='

# Class for the Bendover bot
class Bendover(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.songQueue = SongQueue()
        self.service = build('youtube', 'v3', developerKey=keys.google_api_key)
        self.voiceState = None

    def getTitleAndVideoId(self, msg):
        request = self.service.search().list(
            part='snippet',
            maxResults=1,
            type='video',
            q=msg
        )
        video = request.execute()['items'][0]
        title = video['snippet']['title']
        video_id = video['id']['videoId']
        return title, video_id
    
    async def connect(self, ctx, voice_channel):
        print(voice_channel)

    # Play command
    @commands.command(name='play', aliases=['p'])
    async def _play(self, ctx : commands.Context, *args):
        self.voiceState = ctx.author.voice
        if (self.voiceState == None):
            await ctx.channel.send('Bur, join a voice channel')
        else:
            search_terms = ' '.join(args)
            title, id = self.getTitleAndVideoId(search_terms)
            voice_channel = self.voiceState.channel
            vc = ctx.voice_client
            print(vc)

    # Leave command, disconnects the bot
    @commands.command(name='leave', aliases=['adios', 'l', 'quit'])
    async def _leave(self, ctx, *args):
        await ctx.channel.send('Fuck this shit im out')
        await self.bot.close()

# Instantiating the bot

bot = commands.Bot('-', )
bot.add_cog(Bendover(bot))

@bot.event
async def on_ready():
    print("Yer")

@bot.event
async def on_ctx(ctx):
    await bot.process_commands(ctx)

bot.run(keys.TOKEN)