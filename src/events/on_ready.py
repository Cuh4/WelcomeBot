
# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] On Ready
# // ---------------------------------------------------------------------

# // ---- Imports
import discord

from helpers import discord as discordHelpers
from helpers import general as helpers

# // ---- Main
@helpers.events.getSavedEvent("on_ready").attach
async def callback(*args, **kwargs):
    # // get needed vars
    # get discord stuffs
    client: discord.Client = helpers.globals.get("client")
    tree: discord.app_commands.CommandTree = helpers.globals.get("commandTree")
    
    # // main
    # notify
    helpers.prettyprint.success(f"{discordHelpers.utils.formattedName(client.user)} has started.")
    
    # sync
    await tree.sync()