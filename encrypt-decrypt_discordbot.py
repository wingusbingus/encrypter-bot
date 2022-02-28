import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=';', intents=intents)

print('- BOT ONLINE -\n')

# ENCRYPT
@bot.command(name="encrypt", aliases=["enc","encode","cipher"])
async def encrypt(ctx, key='none', *, text='none'):
    if text == 'none':
            await ctx.send('USAGE: ";encrypt (encryption key - no spaces) (text to encrypt)"')
    else:
        keyVal = ['none'] * len(key)
        encText = ['none'] * len(text)
        c = 0
        for char in key:    # 'keyVal[]' has an array of all ASCII chars in 'key'
            keyVal[c] = ord(char)
            c += 1
        c = 0
        for char in text:   # 'encText[]' has an array of all ASCII chars in 'text'
            encText[c] = ord(char) - 32
            encText[c] += keyVal[c % len(key)]
            encText[c] %= 94
            encText[c] = encText[c] + 32
            encText[c] = chr(int(encText[c]))
            c += 1
        encText = ''.join(encText)
        await ctx.send("Encrypted with KEY: " + key)
        await ctx.send(encText)

# DECRYPT
@bot.command(name="decrypt", aliases=["dec","decode","decipher"])
async def decrypt(ctx, key='none', *, text='none'):
    if text == 'none':
            await ctx.send('USAGE: ";decrypt (encryption key - no spaces) (text to decrypt)"')
    else:
        keyVal = ['none'] * len(key)
        encText = ['none'] * len(text)
        c = 0
        for char in key:    # 'keyVal[]' has an array of all ASCII chars in 'key'
            keyVal[c] = ord(char)
            c += 1
        c = 0
        for char in text:   # 'encText[]' has an array of all ASCII chars in 'text'
            encText[c] = ord(char) - 32
            encText[c] -= keyVal[c % len(key)]
            while encText[c] < 0:
                encText[c] += 94
            encText[c] = encText[c] + 32
            encText[c] = chr(int(encText[c]))
            c += 1
        encText = ''.join(encText)
        await ctx.send("Decrypted with KEY: " + key)
        await ctx.send(encText)


#TOKEN#TOKEN#TOKEN#TOKEN#TOKEN#TOKEN#TOKEN#TOKEN#TOKEN#TOKEN#TOKEN#TOKEN
bot.run('')
