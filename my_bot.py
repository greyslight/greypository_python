import discord
from discord.ext import commands
import mycode
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
async def generatepass(ctx):
    await ctx.send("Berapa panjang passwordnya?")
    panjang = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    if panjang.content.isdigit():
        panjang = int(panjang.content)
        await ctx.send(f"Ini passwordnya: {gen_pass(panjang)}")
    else:
        await ctx.send("Eror, ulang lagi. Coba masukkan menggunakan angka(1,3,5...)")


@bot.command()
async def pangkatkan(ctx):
    await ctx.send("angka apa yang anda ingin pangkatkan?")
    angka = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel) #input() versi discord bot
    if angka.content.isdigit(): #isdigit() untuk cek string adalah sebauh interger, isalpha() untuk mengecek string adalah sebuah string
        angka = int(angka.content) #bisa membaca isi dari apa yang kita tulis di chat
        await ctx.send(f'Berikut pangkat dari {angka}')
        await ctx.send(angka**2)
    else:
        await ctx.send("Eror, ulang lagi. Coba masukkan menggunakan angka(1,3,5...)")

@bot.command()
async def soalmtk(ctx):
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    list_hitung = ["+", "-", "x"]
    operator = random.choice(list_hitung)
    print(operator)

    correctRes = 0
    if operator == "+":
        correctRes = a + b
    elif operator == "-":
        if a < b:
            a = b + random.randint(2,10)
        correctRes = a - b
    elif operator == "x":
        correctRes = a*b
    await ctx.send(f"berapa {a} {operator} {b}?")

    tebak = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    tebak = int(tebak.content)
    if tebak == correctRes:
        await ctx.send("Kamu benar!")
    else:
        await ctx.send(f"Maaf kamu salah, jawaban dari {a} {operator} {b} adalah {correctRes}")
    

@bot.command()
async def guess(ctx):
    await ctx.send("tebak angka dari 1 sampai 10")
    jawaban = random.randint(1,10)
    tebak = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    tebak = int(tebak.content)
 
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
        "$guess : bermain tebak angka dengan bot",
        "$soalmtk : bot memberikan soal matematika tentang penjumlahan dan pengurangan"
    ]
    for helpcom in list_command:
        await ctx.send(helpcom)

bot.run('token here')
