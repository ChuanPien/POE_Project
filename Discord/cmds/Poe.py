import discord
from discord.ext import commands
from core.classes import Cog_Extension
import log.log as l
import crawler.ModifiersCalc as M
# import crawler.Shop as S

Word = ('武器', '屬性', '增加', '查', '清', 'clear')
Attr = []
weapen = ""
item = ""

class Poe(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return
    
        if msg.content.startswith(Word):
            l.poe(msg)

        if msg.content.startswith("詞綴"):
            global item
            item = msg.content[2:]
            await self.say(msg, f'武器設定為[{item}]')

        if msg.content.startswith("武器"):
            global weapen
            weapen = msg.content[2:]
            await self.say(msg, f'武器設定為[{weapen}]')

        if msg.content.startswith("屬性"):
            att = msg.content[2:]
            global Attr
            Attr.clear()
            Attr = att.split(' ')
            await self.say(msg, f'屬性設定為{Attr}')

        if msg.content.startswith("增加"):
            att = msg.content[2:]
            Attr.append(att)
            await self.say(msg, f'屬性增加[{att}]')

        if msg.content == '清除武器':
            weapen = ''
            await self.say(msg, '清空完成')

        if msg.content == '清除屬性':
            Attr.clear()
            await self.say(msg, '清空完成')

        if msg.content == '清除詞綴':
            item = ''
            await msg.channel.send('清空完成')

        if msg.content.startswith('查'):
            if not weapen:
                await self.say(msg, '無設定武器/道具')
            else:
                await self.say(msg, f'武器/道具設為 {weapen}')

            if not Attr:
                await self.say(msg, '無設定屬性')
            else:
                await self.say(msg, f'屬性設為 {Attr}')

            if not item:
                await self.say(msg, '無設定詞綴')
            else:
                await self.say(msg, f'詞綴設為 {item}')

        if msg.content == '搜尋詞綴':
            await self.say(msg, '查詢中...')
            if weapen and item:
                img, url = M.mod(item, weapen, Attr)
                with open(f'D:/GoogleDrive/project/Discord/screenshot/{img}.png', 'rb') as f:
                    picture = discord.File(f)
                    
                embed=discord.Embed(title=f"[{weapen}]詞綴網頁", url=f"{url}", description="🔽🔽設定項目🔽🔽", color=0xff0000)
                embed.set_author(name="POE詞綴搜尋")
                embed.set_thumbnail(url="https://i.imgur.com/uycXL5r.png")
                embed.add_field(name=f"道具/武器", value=f"{weapen}", inline=False)
                embed.add_field(name=f"詞綴", value=f"{item}", inline=False)

                if Attr:
                    for att in Attr:
                        embed.add_field(name=f"屬性", value=f"{att}", inline=True)
                else:
                    embed.add_field(name="屬性", value="無設定屬性", inline=True)


                await msg.channel.send(embed=embed)
                await msg.channel.send(file=picture)
            elif weapen:
                url = M.mod(item, weapen, Attr)
                    
                embed=discord.Embed(title=f"[{weapen}]詞綴網頁", url=f"{url}", description="🔽🔽設定項目🔽🔽", color=0xff0000)
                embed.set_author(name="POE詞綴搜尋")
                embed.set_thumbnail(url="https://i.imgur.com/uycXL5r.png")
                embed.add_field(name=f"道具/武器", value=f"{weapen}", inline=False)
                embed.add_field(name="屬性", value="無設定屬性", inline=True)
                embed.add_field(name="詞綴", value="無設定詞綴", inline=True)

                await msg.channel.send(embed=embed)
            else:
                await self.say(msg, '需要設定武器')

        # if msg.content == '搜尋市集':
        #     if not weapen and not Attr:
        #         embed=discord.Embed(title=f"市集首頁", url=f"{Link}", color=0xff0000)
        #         embed.set_author(name="POE市集搜尋")
        #         embed.set_thumbnail(url="https://i.imgur.com/uycXL5r.png")
        #         await msg.channel.send(embed=embed)
        #     elif len(Attr) > 6:
        #         await self.say(msg, '詞綴不能大於6個')
        #     else:
        #         await self.say(msg, '開始查詢')
        #         Link,wea,atts,q = S.shop(weapen, Attr)

        #         embed=discord.Embed(title=f"搜尋結果{q}筆", url=f"{Link}", description="🔽🔽設定項目🔽🔽", color=0xff0000)
        #         embed.set_author(name="POE市集搜尋")
        #         embed.set_thumbnail(url="https://i.imgur.com/uycXL5r.png")
        #         if weapen:
        #             embed.add_field(name=f"道具[{weapen}]", value=f"{wea}", inline=False)
        #         else:
        #             embed.add_field(name="道具", value="無搜尋道具", inline=False)

        #         if Attr:
        #             i=0
        #             for att in Attr:
        #                 embed.add_field(name=f"詞綴[{att}]", value=f"{atts[i]}", inline=True)
        #                 i+=1
        #         else:
        #             embed.add_field(name="詞綴", value="無搜尋詞綴", inline=True)

        #         await msg.channel.send(embed=embed)

    async def say(self, ch, msg):
        await ch.channel.send(msg)


def setup(bot):
    bot.add_cog(Poe(bot))