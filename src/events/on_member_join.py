
# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] On Member Join Event
# // ---------------------------------------------------------------------

# // ---- Imports
import discord
import random

from helpers import discord as discordHelpers
from helpers import general as helpers
import ui

from . import events

# // ---- Main
@events.getSavedEvent("on_member_join").attach
async def callback(**data):
    # // get needed vars
    # get discord stuffs
    client: discord.Client = helpers.globals.get("client")
    member: discord.Member = data.get("member")
    guild = member.guild
    
    # get guild configuration
    guildConfigGlobal: discordHelpers.guildConfig = helpers.globals.get("guildConfig")

    # // basic checks
    # ignore bots
    if member.bot:
        return
    
    # // main
    # get config stuffs
    title = guildConfigGlobal.get(guild, "wm_Title", guild.name)
    message = guildConfigGlobal.get(guild, "wm_Message", "Welcome! Tell the server admins to use /setup.")
    channel_id = guildConfigGlobal.get(guild, "wm_ChannelID", 0)
    
    # get channel
    channel = guild.get_channel(channel_id) or await guild.fetch_channel(channel_id)
    channelError = False
    
    if not channel:
        # cant pick a random channel
        if len(guild.channels) <= 0:
            return 
        
        # pick a random channel
        channel = guild.channels
        channelError = True
        
    # send message
    embed = discord.Embed(
        title = f"👋 | {title}",
        message = {message},
        color = discord.Color.from_rgb(*[random.randint(255, 255, 255) for _ in range(3)])
    )
    
    if channelError:
        embed.set_footer(text = "⚠ | Something went wrong with choosing a channel. Please tell a server admin to use the /setup command.")
    
    await channel.send(
        content = discordHelpers.utils.mentionUser(member),
        embed = embed
    )