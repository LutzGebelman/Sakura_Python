import discord, os, random, shityshit, asyncio, youtube_dl, discord_music
from discord.ext import commands, tasks
token = 'token here'
i = 0
bot = commands.Bot(command_prefix = 's!')


@bot.event
async def on_ready():
    print('Bot is ready')
    server_checker.start()
    
@bot.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left a server')

@bot.command()
async def play(ctx, url):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    
    def leave():
        print("leaving")
        disc = vc.disconnect()
        fut = asyncio.run_coroutine_threadsafe(disc, bot.loop)
        try:
            fut.result()
        except:
            # an error happened sending the message
            pass
        
    song_list = []
    song_list.append(discord_music.play(url)[1])
    await ctx.send('playing: ' + url)
    for i in song_list:
        vc.play(discord.FFmpegOpusAudio(song_list[0]), after=lambda e: leave())
        del song_list[0]

@bot.command(help="Shows history of whatever discord id you'll give it")
async def snowflake(ctx, id):
    await ctx.send(discord.utils.snowflake_time(int(id)))

@bot.command()
async def is_in_ch(ctx):
    channl = ctx.message.author.voice.channel

            
    print(channl)


@bot.command(help="Shows application info")
async def about_me(ctx):
    data = await bot.application_info()
    await ctx.send(data)

@bot.command(help="helps you choose between two options")
async def choose(ctx, *args):
    await ctx.send(args[random.randrange(0, len(args))])

@bot.command()
async def rand(ctx, from_num, to_num, num_of_runs):
    message = []
    if Exception == discord.ext.commands.errors.MissingRequiredArgument:
        num_of_runs = 1
    num_of_runs = int(num_of_runs)

    for i in range(num_of_runs):
        message.append(random.randrange(int(from_num), int(to_num)))
    await ctx.send(message)

@bot.command()
async def topic(ctx, topic_arg):
    channelid = ctx.channel.id
    try:
        await bot.get_channel(channelid).edit(topic=topic_arg)
        await ctx.send("status changed")
    except discord.errors.Forbidden:
        await ctx.send('Missing Permissions')

@bot.command()
async def playerlist(ctx):
    playerlist = shityshit.playerlist()
    await ctx.send(playerlist)

@bot.command()
async def player_count_here(ctx):
    global channel_to_change_topic_in
    channel_to_change_topic_in = ctx.channel.id
    print("forwarding ", channel_to_change_topic_in)
    topic_changer.start()
    await ctx.send('Server data will now display in the topic of this chat') 
    

@bot.command()
async def message(ctx, msg):
    await ctx.send(ctx.message.content)

@bot.command()
async def stop_player_count(ctx):
    topic_changer.stop()
    await bot.get_channel(channel_to_change_topic_in).edit(topic='')

@bot.command()
async def guild_avatar(ctx): # sends guild icon
    guild = ctx.guild
    avatar = guild.icon_url
    await ctx.send(avatar)

@bot.command()
async def avatar(ctx, user: discord.User): # sends avatar of user
    await ctx.send(user.avatar_url)

@bot.command()
async def ddos(ctx, uid: discord.User, num_of_ms):
    for i in range(int(num_of_ms)):
        await uid.send('stop singing bitch')

@bot.command()
async def tiktaktow(ctx):
    tik_tac_tow.Game(ctx)

@tasks.loop(seconds=5.0)
async def server_checker():
    player_count = shityshit.playercount()
    await bot.change_presence(activity=discord.Game(player_count))
    
@tasks.loop(seconds=5.0)
async def topic_changer():
    player_count = shityshit.playercount()
    await bot.get_channel(channel_to_change_topic_in).edit(topic=player_count)

bot.run(token)
