# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Template Modal UI
# // ---------------------------------------------------------------------

# // ---- Imports
import discord

import config

# // ---- Main
# // UI
class modal(discord.ui.Modal):
    def setup(self, title: str):
        super().__init__(title = title, timeout = config.uiModalTimeout)