# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Setup Slash Command
# // ---------------------------------------------------------------------

# // ---- Imports
import discord

import ui
from helpers import general as helpers
from helpers import discord as discordHelpers

# // ---- Main
# // get vars
# discord-related
client: discord.Client = helpers.globals.get("client")
tree: discord.app_commands.CommandTree = helpers.globals.get("commandTree")

# // main command
# slash command
@tree.command(
    name = "setup",
    description = "Set up your server for the bot."
)
@discord.app_commands.describe(channel = "The channel that welcome messages will be sent in.")
async def command(interaction: discord.Interaction, channel: discord.TextChannel):
    # // checks
    # setup
    checks = helpers.misc.failChecks()
    
    # permissions check
    if not discordHelpers.utils.hasPermissions(client, interaction.user, ["manage_guild"]):
        checks.fail("You need `manage_guild` permissions to run this command.")
        
    # failure message if failed
    failed, failureMessage = checks.result()
    
    if failed:
        return await interaction.response.send_message(
            embed = discordHelpers.embeds.failure(failureMessage),
            ephemeral = True
        )
        
    # // main
    # show modal
    await interaction.response.send_modal(ui.modals.setup(interaction.guild, channel))