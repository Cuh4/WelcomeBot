# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Main
# // ---------------------------------------------------------------------

# // ---- Imports
import discord
import time
import random

import config
import slashCommands
from events import events
from helpers import discord as discordHelpers
from helpers import general as helpers

# // ---- Variables
# // Discord
# intents
intents = discord.Intents.default()
intents.message_content = True

# client
client = discord.Client(
    intents = intents,
    
    status = discord.Status.do_not_disturb,
    activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = config.activityText
    )
)

tree = discord.app_commands.CommandTree(client)

# // ---- Main
# // Register Globals
# bot
helpers.globals.save("client", client)
helpers.globals.save("commandTree", tree)
helpers.globals.save("startupTimestamp", time.time())

# main
helpers.globals.save("guildConfig", discordHelpers.guildConfig("data"))

# // Register Commands
slashCommands.start()

# // Discord Events
# On Ready
@client.event
async def on_ready():
    await events.on_ready.asyncFire()

# On Message
@client.event
async def on_message(message: discord.Message):
    await events.on_message.asyncFire(
        message = message
    )
    
# On Member Join
@client.event
async def on_member_join(member: discord.Member):
    await events.on_member_join.asyncFire(
        member = member
    )
    
# // Start Bot
client.run(config.botToken)