# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Main
# // ---------------------------------------------------------------------

# // ---- Imports
import discord
import time
import random

import config
import slashCommands
import events
from helpers import discord as discordHelpers
from helpers import general as helpers

# // ---- Variables
# // Discord
# Intents
intents = discord.Intents.default()
intents.members = True

# Bot
client = discord.Client(
    intents = intents,
    
    status = discord.Status.do_not_disturb,
    activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = config.activityText
    )
)

# Commands
tree = discord.app_commands.CommandTree(client)

# // ---- Main
# // Register Globals
# Bot
helpers.globals.save("client", client)
helpers.globals.save("commandTree", tree)
helpers.globals.save("startupTimestamp", time.time())

# Main
helpers.globals.save("guildConfig", discordHelpers.guildConfig("data"))

# // Register Commands
slashCommands.start()

# // Bot Ready
@client.event
async def on_ready():
    await events.setup(client)
    await helpers.events.getSavedEvent("on_ready").asyncFire()
    
# // Start Bot
client.run(config.botToken, log_handler = None)