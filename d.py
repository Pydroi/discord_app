import discord
import random
from pyautogui import *
import pyautogui
import time
import os
import asyncio
import youtube_dl


TOKEN ="MTAyMTM1NjI3Mjk1MzYxMDI1MA.GQFRvh.UEga0bWFM4jAFrwOjBi9K1Lz_zng-NJhFLyNfg"

client = discord.Client()

block_words =["fuck","bitch"]

voice_clients={}
yt_dl_opts ={"formats":"bestaudio/best"}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options ={"options":"-vn"}

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")
    




@client.event
async def on_message(message):
    print(f"Bot logged in as {client.user}")
    username = str(message.author).split("#")[0]
    user_message = message.content
  
    channel =str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")
    
    
    if message.author == client.user:
        return
    
        
    #await message.channel.send(user_message)
    
    
    if message.content == 'ping':
            await message.channel.send('pong')
    
    
    
    if message.content.lower()=='hi':
        await message.channel.send(f"hello  {username}")
        return

    elif user_message.lower() == "bye":
        await message.channel.send(f"see you later {username}!")
        return
    
    elif user_message.lower() =="random":
        response =f"This is your random number: {random.randrange(1000000)}"
        await message.channel.send(response)
        return
    if user_message.lower() =="anywhere":
        await message.channel.send("This can be used anywhere!")
        return 

    if user_message.lower() =="spam":
        for i in range(1,(10)):
                await message.channel.send("hii")
    
    if (user_message.lower()=="kick") :
        print(message.channel.name)
         #   await message.slayer_ts.send("it works")

    

    
    if message.author != client.user:
        for text in block_words:
            if "Moderator" not in str(message.author.roles) and text in str(message.content.lower()):
                await message.delete()
                await message.channel.send(f"No swearing {username} !!")
                return
        print("Not Deleting...")
    
    
    if message.content.startswith("play"):
        try:
           voice_client = await message.author.voice.channel.connect()
           vocie_clients[voice_client.guild.id]=voice_client
        
        
        except:
            pass
            #print("error")
        
        try:
            url = message.content[len('play'):].strip()
            
            
             
            loop=asyncio.get_event_loop()
            data =await loop.run_in_executor(None, lambda:ytdl.extract_info(url,download=False))
            
            song=data['url']
            player=discord.FFmpegPCMAudio(song, **ffmpeg_options)
            
            voice_clients.play(player)
        except Exception as err:
            print(err)
    
    if message.content.startswith("pause"):
        try:
            voice_clients[message.guild.id].pause()

        except Exception as err:
            print(err)

    
    if message.content.startswith("stop"):
        voice_client = message.guild.voice_client

        # Stop playing and disconnect
        #voice_client.stop()
        await voice_client.disconnect()







client.run(TOKEN)
