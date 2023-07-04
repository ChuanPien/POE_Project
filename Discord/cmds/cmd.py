from discord.ext import commands
from core.classes import Cog_Extension
import linecache, os, glob

class Main(Cog_Extension):

    @commands.command(help = "偵測與伺服器連線品質")
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command(help = "覆誦文字")
    async def rep(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command(help = "清除文字")
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)
        await ctx.send(f'{num} msg clean Succ')

    @commands.command(aliases = ['qalog','查詢紀錄'], help = "查詢搜尋紀錄(同指令 : 查詢紀錄/qalog)")
    async def log(self, ctx, num: int):
        await ctx.send('搜尋中...')
        if os.path.isfile(f"./QA/{ctx.author.id}.txt"):
            j = 0
            with open(f"./QA/{ctx.author.id}.txt", 'r', encoding = 'utf8') as f:
                total_lines = sum(1 for line in f)
                await ctx.send(f'共{total_lines}筆查詢紀錄')
                for i in range(total_lines, total_lines - num, -1):
                    await ctx.send(f)
                    j += 1
                    if linecache.getline(f"./QA/{ctx.author.id}.txt", i) == "":
                        break
                    else:
                        await ctx.send(linecache.getline(f"./QA/{ctx.author.id}.txt", i))
                await ctx.send(f'搜尋完成，共{j}筆.')
        else:
            await ctx.send('還沒提問過呦~')

    @commands.command(aliases = ['ds'], help = "清空螢幕截圖資料夾(同指令 : ds)")
    async def delscr(self, ctx):
        await ctx.send(f'清除中...')
        files = glob.glob("D:/GoogleDrive/project/Discord/screenshot/*")
        for f in files:
            os.remove(f)
        await ctx.send(f'清除完成')

    # @commands.command(aliases = ['rl'], help = "訓練AI(同指令 : rl)")
    # async def relearn(self, ctx, num: int):
    #     await ctx.send(f'開始訓練 {num}次')
    #     j = 0
    #     for i in range(num):
    #         j += 1
    #     await ctx.send(f'訓練完成 {j}次')
        
def setup(bot):
    bot.add_cog(Main(bot))