
# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] On Message Event
# // ---------------------------------------------------------------------

# // ---- Imports
import discord

from helpers import discord as discordHelpers
from helpers import general as helpers

from . import events

# // ---- Main
@events.getSavedEvent("on_message").attach
async def callback(*args, **kwargs):
    pass