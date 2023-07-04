import discord
from discord.ext import commands
from core.classes import Cog_Extension
import ModifiersCalc as M   #導入 ModifiersCalc.py 並告成 M

Attr = []   #宣告屬性列表
weapen = "" #宣告武器字串
item = ""   #宣告詞綴字串

class Poe(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        
        if msg.author == self.bot.user: #偵測是否是BOT自己說話，是的話就無視
            return
        
        if msg.content.startswith("詞綴"):  #若使用者輸入的文字開頭是"詞綴"
            global item
            item = msg.content[2:]  #刪去開頭"詞綴"二字，保留後面的
            await msg.channel.send(f'武器設定為[{item}]')
        
        if msg.content.startswith("武器"):  #若使用者輸入的文字開頭是"武器"
            global weapen
            weapen = msg.content[2:]  #刪去開頭"武器"二字，保留後面的
            await msg.channel.send(f'武器設定為[{weapen}]')
        
        if msg.content.startswith("屬性"):  #若使用者輸入的文字開頭是"屬性"
            att = msg.content[2:]   #刪去開頭"屬性"二字，保留後面的
            global Attr
            Attr.clear()  #保險，清空屬性列表
            Attr = att.split(' ')   #用空格分割att字串，並放入Attr列表中
            await msg.channel.send(f'屬性設定為{Attr}')

        if msg.content.startswith("增加"):  #若使用者輸入的文字開頭是"增加"
            att = msg.content[2:]   #刪去開頭"增加"二字，保留後面的
            Attr.append(att)    #放入Attr列表中
            await msg.channel.send(f'屬性增加[{att}]')
        
        if msg.content == '清除武器':   #若使用者輸入的文字是"清除武器"
            weapen = ''  #清空武器
            await msg.channel.send('清空完成')
        
        if msg.content == '清除屬性':   #若使用者輸入的文字是"清除屬性"
            Attr.clear()    #清空屬性
            await msg.channel.send('清空完成')
        
        if msg.content == '清除詞綴':   #若使用者輸入的文字是"清除詞綴"
            item = ''   #清空詞綴
            await msg.channel.send('清空完成')

        if msg.content.startswith('查'):    #若使用者輸入的文字開頭是"查"，BOT回復目前使用者的所有設定
            if not weapen:  #如果沒有設定武器
                await msg.channel.send('無設定武器/道具')
            else:
                await msg.channel.send(f'武器/道具設為 {weapen}')

            if not Attr:    #如果沒有設定屬性
                await msg.channel.send('無設定屬性')
            else:
                await msg.channel.send(f'屬性設為 {Attr}')

            if not item:    #如果沒有設定詞綴
                await msg.channel.send('無設定詞綴')
            else:
                await msg.channel.send(f'詞綴設為 {item}')

        if msg.content.startswith == '搜尋':    #若使用者輸入的文字開頭是"搜尋"
            await msg.channel.send('查詢中...')    #BOT回復訊息表示收到
            if weapen and item: #如果有設定武器及詞綴
                img, url = M.mod(item, weapen, Attr)    
                #呼叫crawler/ModifiersCalc.py中的mod function
                #將詞綴(item)/武器(weapon)/屬性(Attr)傳過去
                #接收M.mod回傳的值，放入img(截圖檔名)及url(網址)中

                with open(f'D:/GoogleDrive/project/Discord/screenshot/{img}.png', 'rb') as f:   #開啟截圖資料夾，並透過img參數選擇正確的圖片
                    picture = discord.File(f)   #將檔案宣告成 picture

                #宣告並設定Embed
                embed=discord.Embed(title=f"[{weapen}]詞綴網頁", url=f"{url}", description="🔽🔽設定項目🔽🔽", color=0xff0000)
                embed.set_author(name="POE詞綴搜尋")
                embed.set_thumbnail(url="https://i.imgur.com/uycXL5r.png")
                embed.add_field(name=f"道具/武器", value=f"{weapen}", inline=False)
                embed.add_field(name=f"詞綴", value=f"{item}", inline=False)

                if Attr:    #如果有設定屬性，就將他加入Embed
                    for att in Attr:
                        embed.add_field(name=f"屬性", value=f"{att}", inline=True)
                else:
                    embed.add_field(name="屬性", value="無設定屬性", inline=True)


                await msg.channel.send(embed=embed)  #BOT將Embed畫面輸出
                await msg.channel.send(file=picture) #BOT將照片輸出
            elif weapen:   #若只有設定武器
                url = M.mod(item, weapen, Attr)
                #呼叫crawler/ModifiersCalc.py中的mod function
                #將詞綴(item)/武器(weapon)/屬性(Attr)傳過去
                #接收M.mod回傳的值放入url(網址)中

                #宣告並設定Embed
                embed=discord.Embed(title=f"[{weapen}]詞綴網頁", url=f"{url}", description="🔽🔽設定項目🔽🔽", color=0xff0000)
                embed.set_author(name="POE詞綴搜尋")
                embed.set_thumbnail(url="https://i.imgur.com/uycXL5r.png")
                embed.add_field(name=f"道具/武器", value=f"{weapen}", inline=False)
                embed.add_field(name="屬性", value="無設定屬性", inline=True)
                embed.add_field(name="詞綴", value="無設定詞綴", inline=True)

                await msg.channel.send(embed=embed)  #BOT將Embed畫面輸出
            else:   #通知使用者至少需要設定"武器"
                await msg.channel.send('需要設定武器')


def setup(bot):
    bot.add_cog(Poe(bot))