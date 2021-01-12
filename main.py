import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_voice_state_update(member, prev, cur):
    user = f"{member.name}#{member.discriminator}"
    vc = member.guild.voice_client
    if cur.self_mute and not prev.self_mute: # Would work in a push to talk channel
        print(f"{user} stopped talking!")
        if not vc.is_playing():
            vc.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source="mic_click_on.wav"))
            vc.source = discord.PCMVolumeTransformer(vc.source)
            vc.source.volume = 0.5
    elif prev.self_mute and not cur.self_mute: # As would this one
        print(f"{user} started talking!")
        if not vc.is_playing():
            vc.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source="mic_click_off.wav"))
            vc.source = discord.PCMVolumeTransformer(vc.source)
            vc.source.volume = 0.5


@client.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
    else:
        await ctx.send("You are not connected to a voice channel")
        return
    await channel.connect()


@client.command(pass_context=True)
async def leave(ctx):
    await ctx.voice_client.disconnect()

client.run(TOKEN)
