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
# intents
intents = discord.Intents.default()
intents.members = True

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
events.setup()
    
# // Start Bot
client.run(config.botToken)