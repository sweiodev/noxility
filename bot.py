from discord.ext import commands
import discord, os, asyncio, logging


bot = commands.Bot(command_prefix=['nox ', 'Nox ', 'NOX '], owner_id=199375184057073664, intents=discord.Intents.all())

bot.remove_command("help")

for cog in os.listdir("cogs"):
    if cog.endswith(".py"):
        if cog != "__init__.py":
            try:
                cog = f"cogs.{cog.replace('.py', '')}"
                bot.load_extension(cog)
                print(f"{cog} loaded.")
            except Exception as e:
                print(f"{cog} couldn't be loaded.")
                raise e        

@bot.command()
@commands.is_owner()
async def reload(ctx, cog=None):
    """
    Usage: <prefix> reload <cog>
    It reloads a cog. You can use this if a cog is not working correctly.
    """
    cogs = []
    for cogg in os.listdir("cogs"):
        if cogg.endswith(".py"):
            if cogg != "__init__.py":
                cogs.append(cogg)
    if cog is None: await ctx.send(f"Please specify which cog to reload. Available cogs: {', '.join(cogs)}.")
    else:
        try:
            bot.unload_extension(f"cogs.{cog}")
            bot.load_extension(f"cogs.{cog}")
            await ctx.send(f"Successfully reloaded {cog}.")
            print(f"Reloaded {cog}.")
        except Exception as e:
            await ctx.send(f"I couldn't reload {cog}.")
            print(f"{cog} couldn't be reloaded.")
            raise e

@bot.command(aliases=['disconnect', 'close', 'stopbot'])
@commands.is_owner()
async def logout(ctx):
    await ctx.send("Noxility logging out.")
    await bot.logout()

"""
# logging system
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
"""

bot.run("Nzg1MTI4MjI4MjEyNzAzMjMz.X8zVpA.uPGZzBpz1sW6LXEtUoPzW8W52zo")