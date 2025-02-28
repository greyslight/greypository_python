import discord
from discord.ext import commands
from mycode import gen_pass
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def laugh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def generatepass(ctx, length = 5):
    await ctx.send(gen_pass(length))

@bot.command()
async def pangkatkan(ctx):
    await ctx.send("angka apa yang anda ingin pangkatkan?")
    angka = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel) #input() versi discord bot
    if angka != int():
        await ctx.send("Eror, ulang lagi. Coba masukkan menggunakan angka(1,3,5...)")
    angka = int(angka.content) #bisa membaca isi dari apa yang kita tulis di chat

    await ctx.send(f'Berikut pangkat dari {angka}')
    await ctx.send(angka**2)

@bot.command()
async def guess(ctx):
    await ctx.send("tebak angka dari 1 sampai 10")
    jawaban = random.randint(1,10)
    tebak = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)

    if tebak == jawaban:
        await ctx.send("Kamu benar!")
    else:
        await ctx.send(f"Maaf kamu salah, jawabannya {jawaban}")

@bot.command()
async def showcommands(ctx):
    await ctx.send("Ini semua command dari bot ini:")
    list_command = [
        "$hello : menyapa bot",
        "$laugh(optional pakai angka): membuat bot tertawa",
        "$generatepass(dengan angka untuk panjang password) : mengenerate password random",
        "$pangkatkan(dengan angka) : mempangkat 2 sebuah angka",
    ]
    for helpcom in list_command:
        await ctx.send(helpcom)

bot.run('token here')
