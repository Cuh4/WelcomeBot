# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Template Modal UI
# // ---------------------------------------------------------------------

# // ---- Imports
import discord

import config
import ui
from ui.modals import template
from helpers import general as helpers
from helpers import discord as discordHelpers

# // ---- Main
# // UI
class modal(template):
    # // Main UI
    def __init__(self, guild: discord.Guild, desiredWelcomeChannel: discord.TextChannel):
        # // setup
        # init
        self.setup("Setup")
        
        # attributes
        self.guildConfig: discordHelpers.guildConfig = helpers.globals.get("guildConfig")
        self.desiredChannel = desiredWelcomeChannel
        self.guild = guild
        
        # // title input
        # create
        self.titleInput = discord.ui.TextInput(
            label = "Welcome Message - Title",
            placeholder = "My Server",
            max_length = 75
        )
        
        # add to modal
        self.add_item(self.titleInput)
        
        # // message input
        # create
        self.messageInput = discord.ui.TextInput(
            label = "Welcome Message - Message",
            placeholder = "Welcome to my very awesome server!\nWoohoo!\n**Markdown is __supported__.**",
            max_length = 2000,
            style = discord.TextStyle.paragraph
        )
        
        # add to modal
        self.add_item(self.messageInput)
      
    # // Callbacks  
    async def on_submit(self, interaction: discord.Interaction):
        # save title
        self.guildConfig.save(
            self.guild,
            "wm_Title",
            self.titleInput.value
        )
        
        # save message
        self.guildConfig.save(
            self.guild,
            "wm_Message",
            self.messageInput.value
        )
        
        # save channel
        self.guildConfig.save(
            self.guild,
            "wm_ChannelID",
            self.desiredChannel.id
        )
        
        # notify user
        await interaction.response.send_message(
            embed = discordHelpers.embeds.success("Successfully set up the bot for your server.")
        )