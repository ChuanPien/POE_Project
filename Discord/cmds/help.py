import discord
from discord.ext import commands

async def send_embed(ctx, embed):
    await ctx.send(embed=embed)

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['h'], help = '呼叫幫助介面(同指令 : h)')
    async def help(self, ctx, *input):
        if not input:
            emb = discord.Embed(title='CPD憨憨', color = discord.Color.blue(),description = f'歡迎使用憨憨機器人\n')
            emb.set_thumbnail(url="https://i.imgur.com/4adIhXS.jpg")

            cmds = ''
            for cmd in self.bot.commands:
                if cmd.cog:
                    cmds += f'{cmd.name} - {cmd.help}\n'

            commands_desc = ''
            for command in self.bot.walk_commands():
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'

            emb.add_field(name = '---需前墜指令---', value = cmds, inline = False)
            emb.add_field(name = '---觸發指令---', value = 'dcard / time', inline = False)
            emb.add_field(name = '---伺服端指令---', value = commands_desc, inline = False) 
            emb.add_field(name = "關於", value = f"因大學專題而產生地機器人")
            emb.set_footer(text = f"Developed by ChuanPien#3075")
        await send_embed(ctx, emb)


def setup(bot):
    bot.add_cog(Help(bot))