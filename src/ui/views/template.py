# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Template View UI
# // ---------------------------------------------------------------------

# // ---- Imports
import discord

import config

# // ---- Main
class view(discord.ui.View):
    message: discord.Message = None
    
    # // methods
    def setup(self):
        super().__init__(timeout = config.uiViewTimeout)

    def setViewMessage(self, message: discord.Message):
        self.message = message
    
    # // discord callbacks
    async def on_timeout(self):
        if self.message is None:
            return
        
        # disable items
        for item in self.children:
            # disable all buttons
            if isinstance(item, discord.ui.Button):
                # ignore url buttons
                if item.style == discord.ButtonStyle.url:
                    continue
                
                # disable button
                item.disabled = True
    
        # save changes
        return await self.message.edit(
            view = self
        )