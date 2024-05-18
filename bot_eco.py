import discord
from discord.ext import commandsimport discord
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def raccolta_differenziata(ctx):
    await ctx.send("Ecco un vidio che ti spiega cosa è la raccolta differenziata:'https://youtu.be/mDpK_MNOg94'")
@bot.command()
async def riciclo_plastica(ctx):
    await ctx.send("Ecco un vidio che ti spiega come si ricicla la plastica:'https://youtu.be/WALo6GLp_to'")
@bot.command()
async def riciclo_vetro(ctx):
    await ctx.send("Ecco un vidio che ti spiega come si ricicla l'alluminio:'https://youtu.be/QSQa1bZ_hGQ'")
    
bot.run( "scrivi il tuo token" )
