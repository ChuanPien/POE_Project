from discord.ext import commands
from core.classes import Cog_Extension
import crawler.dcard as d
import log.log as l
import datetime, json, discord
with open('setting.json', 'r', encoding='utf8') as J:
    j = json.load(J)
    
class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        ch = self.bot.get_channel(j['inout'])
        await ch.send(f'{member} Join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        ch = self.bot.get_channel(j['inout'])
        await ch.send(f'{member} Leave!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("缺少參數")
        else:
            print(error)

    @commands.Cog.listener()
    async def on_message(self, msg):
        l.log(msg)
        if msg.author == self.bot.user:
            return

        if msg.content == 'dcard':
            await self.say(msg,'等等嘿')
            arr = d.start()
            embed = discord.Embed(title='Dcard', color = discord.Color.blue())
            for row in arr:
                embed.add_field(name = row[0], value = row[1], inline = False)
            await msg.channel.send(embed = embed)

        if msg.content == 'time':
            day = datetime.datetime.today()
            day = day.strftime("%Y/%m/%d %H:%M:%S")
            await self.say(msg,day)
    
    async def say(self, ch, msg):
        await ch.channel.send(msg)

def setup(bot):
    bot.add_cog(Event(bot))