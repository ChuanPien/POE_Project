import os, json, datetime, discord
from discord.ext import commands
with open('setting.json', 'r', encoding='utf8') as J:
    j = json.load(J)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents = intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    date = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print(f'---------------------------------------')
    print(date)
    print(f'機器人啟動 登入身份：{bot.user}')
    print(f'---------------------------------------')

@bot.command(aliases = ['l'], help = "載入未啟動的檔案")
async def load(ctx, ext):
    bot.load_extension(f'cmds.{ext}')
    await ctx.send(f'Load {ext}.py Succ')

@bot.command(aliases = ['u'], help = "停止已啟動的檔案")
async def unload(ctx, ext):
    bot.unload_extension(f'cmds.{ext}')
    await ctx.send(f'Unload {ext}.py Succ')

@bot.command(aliases = ['r'], help = "重新載入啟動的檔案")
async def reload(ctx, ext):
    bot.reload_extension(f'cmds.{ext}')
    await ctx.send(f'Reload {ext}.py Succ')

for name in os.listdir('./cmds'):
    if name.endswith('.py'):
        bot.load_extension(f'cmds.{name[:-3]}')
        print(f'Load - {name}')


if __name__ == "__main__":
    bot.run(j['Token'])