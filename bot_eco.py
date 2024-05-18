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
async def riciclo_alluminio(ctx):
    await ctx.send("Ecco un vidio che ti spiega come si ricicla l'alluminio:'https://youtu.be/QSQa1bZ_hGQ'")
@bot.command()
async def riciclo_vetro(ctx):
    await ctx.send("Ecco un vidio che ti spiega come si ricicla il vetro:'https://youtu.be/QJNBtzPshVU'")
@bot.command()
async def riciclo_batterie(ctx):
    await ctx.send("Ecco un vidio che ti spiega come si riciclano le batterie:'https://youtu.be/nIWDMpSU6iI'")
@bot.command()
async def riciclo_pneumatici(ctx):
    await ctx.send("Ecco un vidio che ti spiega come si riciclano i pneumatici:'https://youtu.be/QTAlsSdNvV8'")
@bot.command()
async def insegnamenti(ctx):
    await ctx.send("1. compra solo l'essenziale")
    await ctx.send("2. Se possiedi degli oggetti rotti, cerca di ripararli prima di buttarli")
    await ctx.send("3. usa il dettersivo alla spina")
    await ctx.send("4. cerca di comprare il minor numero di oggetti in plastica")
bot.run( "scrivi il tuo token" )
