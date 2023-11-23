# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Quote View UI
# // ---------------------------------------------------------------------

# // ---- Imports
import discord

import config
import ui
from ui.views import template
from helpers import general as helpers
from helpers import discord as discordHelpers

# // ---- Main
# // UI
class view(template):
    # // Main UI
    def __init__(self):
        # // setup
        # setup template
        super().setup()
        
        # // get variables
        # foundation variables
        self.client: discord.Client = helpers.globals.get("client")

        # // discord invite button
        # create button
        self.inviteButton = discord.ui.Button(
            label = "Support Server",
            url = "https://discord.gg/2HR2awsdSt",
            emoji = "😎"
        )
        
        # add
        self.add_item(self.inviteButton)