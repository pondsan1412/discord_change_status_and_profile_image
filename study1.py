import discord
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
import requests
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event #เมื่อมีเหตการ บอทออนไลน์ บอทจะ ปริ้น logged in as บลาๆ
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
   
@bot.command() 
async def set_avatar(ctx, url): #โดยการใช้งานนั้นคือการแทรกลิ้ง url ของรูปภาพ !set_avatar [url]
    img = requests.get(url).content
    await bot.user.edit(avatar=img)
    await ctx.send('เปลี่ยนรูปโปรบอทเรียบร้อยแล้ว!')
@bot.command()
async def set_status(ctx, status):# โดยการใช้งาน !set_status [ชอบกินไก่ทอด] 
    activity = discord.Game(name=status)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    await ctx.send(f'เปลี่ยนสถานะของบอทเป็น `{status}`!')
    
load_dotenv()
token = os.getenv("TOKEN2") #ตรงส่วนนี้ต้องกำหนดตัวแปรข้างใน env
bot.run(token) #ตัวแปร token จะเก็บค่า str ของ token เอาไว้ใน ไฟล์ env

